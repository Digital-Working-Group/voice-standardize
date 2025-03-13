"""
pydub_standardize.py
standardize via pydub
"""
import os
from pydub import AudioSegment

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

def get_outpath_and_infile_ext(audio_fp, out_root, out_fmt, parameter_dict):
    """
    construct an outpath based on the audio_fp and parameters;
    """
    audio_base, infile_ext = os.path.splitext(os.path.basename(audio_fp))
    out_fname = f'{audio_base}.{out_fmt}'
    parameter_ext = '_'.join([f'{k}_{v}' for k, v in parameter_dict.items()])
    parameter_ext = parameter_ext.replace("-", "").replace(":", "-")
    ## remove front - and : not allowed in Windows paths;
    out_parent_dir = os.path.join(os.path.dirname(audio_fp), out_root, parameter_ext)
    if not os.path.isdir(out_parent_dir):
        os.makedirs(out_parent_dir)
    return os.path.join(out_parent_dir, out_fname), infile_ext

def standardize(audio_fp, **kwargs):
    """
    standardize audio_fp via pydub using the given keyword arguments;
    """
    sampling_rate = kwargs.get('sampling_rate')
    out_fmt = kwargs.get('out_fmt', 'wav')
    out_encoding = kwargs.get('out_encoding', 'pcm_s16le')
    out_ffmpeg_kw = kwargs.get('out_ffmpeg_kw', {})
    parameter_dict = {'ar': sampling_rate, 'c:a': out_encoding}
    parameter_dict.update(out_ffmpeg_kw)
    out_root = kwargs.get('out_root', 'pydub')

    outpath, infile_ext = get_outpath_and_infile_ext(audio_fp, out_root, out_fmt, parameter_dict)
    parameters = get_parameters(parameter_dict)
    infile = AudioSegment.from_file(audio_fp, )
    infile.export(outpath, format=out_fmt, parameters=parameters)
    print(outpath)
