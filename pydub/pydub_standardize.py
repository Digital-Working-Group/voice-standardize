"""
pydub_standardize.py
standardize via pydub
"""
import os
import csv
from pydub import AudioSegment
from pydub.utils import mediainfo

def get_parameters(parameter_dict):
    """
    parameter_dict: k=ffmpeg_switch, v=parameter_value
    convert to:
        [ffmpeg_switch, parameter_value, ...]
    """
    parameters = []
    for ffmpeg_switch, parameter_value in parameter_dict.items():
        parameters.extend([f'-{str(ffmpeg_switch)}', str(parameter_value)])
    return parameters

def write_csv(filename, data):
    """
    Writes to a csv file
    """
    with open(filename, 'w', newline= '') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)

def validate_metadata(filepath, parameter_dict, raise_error):
    """
    Compares metadata from output to expected values
    """
    mismatch = []
    map_keys = {'ac': 'channels',
                'ar': 'sample_rate',
                'c:a': 'codec_name'}
    info = mediainfo(filepath)
    for option in parameter_dict:
        if str(parameter_dict[option]) != info[map_keys[option]]:
            mismatch.append([option, parameter_dict[option], info[map_keys[option]]])
    if mismatch != []:
        filename = os.path.splitext(os.path.basename(filepath))[0]
        mismatch.insert(0, ['option', 'expected', 'actual'])
        write_csv(f'validate/{filename}.csv', mismatch)
    if raise_error:
        assert mismatch == [], f'See differences found during validation of metadata: validate/{filename}.csv'
    
def get_outpath(audio_fp, out_root, out_fmt, parameter_dict):
    """
    Construct an outpath based on the audio_fp and parameters;
    """
    audio_base, infile_ext = os.path.splitext(os.path.basename(audio_fp))
    out_fname = f'{audio_base}.{out_fmt}'
    parameter_ext = '_'.join([f'{k}_{v}' for k, v in parameter_dict.items()])
    parameter_ext = parameter_ext.replace("-", "").replace(":", "-")
    ## remove front - and : not allowed in Windows paths;
    out_parent_dir = os.path.join(os.path.dirname(audio_fp), out_root, parameter_ext)
    out_parent_dir = os.path.join(os.path.dirname(audio_fp), out_root, parameter_ext)
    if not os.path.isdir(out_parent_dir):
        os.makedirs(out_parent_dir)
    return os.path.join(out_parent_dir, out_fname)

def standardize(audio_fp, **kwargs):
    """
    standardize audio_fp via pydub using the given keyword arguments;
    """
    sampling_rate = kwargs.get('sampling_rate')
    out_fmt = kwargs.get('out_fmt', 'wav')
    out_encoding = kwargs.get('out_encoding', 'pcm_s16le')
    out_ffmpeg_kw = kwargs.get('out_ffmpeg_kw', {})
    to_mono = kwargs.get('to_mono', False)
    run_validate = kwargs.get('run_validate', False)
    raise_error = kwargs.get('raise_error', False)
    parameter_dict = {'ar': sampling_rate, 'c:a': out_encoding}
    parameter_dict.update(out_ffmpeg_kw)
    if to_mono:
        parameter_dict.update({'ac': 1})
    out_root = kwargs.get('out_root', 'pydub')
    outpath = get_outpath(audio_fp, out_root, out_fmt, parameter_dict)
    parameters = get_parameters(parameter_dict)
    infile = AudioSegment.from_file(audio_fp, )
    infile.export(outpath, format=out_fmt, parameters=parameters)
    if run_validate:
        validate_metadata(outpath, parameter_dict, raise_error)
    print(f'See {outpath} for the standardized audio file.')
