"""
validate.py
Validate standardized audio files against original sample output;
"""
import os
import csv
import hashlib
from pydub_standardize import standardize
from pydub import AudioSegment

def generate_comparison_files():
    """
    main entrypoint
    """
    # All files in sample_audio
    flac_mono = '../sample_audio/flac/mono_first_ten_Sample_HV_Clip.flac'
    flac_stereo = '../sample_audio/flac/first_ten_Sample_HV_Clip.flac'
    mp3_mono = '../sample_audio/mp3/common_voice_en_21635524.mp3'
    mp3_stereo = '../sample_audio/mp3/first_ten_Sample_HV_Clip.mp3'
    m4a_mono = '../sample_audio/m4a/mono_zoom_audio.m4a'
    m4a_stereo = '../sample_audio/m4a/sample_zoom_audio.m4a'
    wav_mono = '../sample_audio/wav/mono_first_ten_Sample_HV_Clip.wav'
    wav_stereo = '../sample_audio/wav/first_ten_Sample_HV_Clip.wav'

    # Convert to 16KHZ wav pcm_s16le
    kwargs = {'sampling_rate': 16000, 'out_fmt': 'wav',
              'out_encoding': 'pcm_s16le', 'run_validate': True,
              'raise_error': True, 'write_meta': True, 'out_root':'test_output'}
    standardize(wav_mono, **kwargs)
    standardize(wav_stereo, **kwargs)
    standardize(flac_mono, **kwargs)
    standardize(m4a_mono, **kwargs)
    standardize(m4a_stereo, **kwargs)
    standardize(mp3_mono, **kwargs)
    standardize(mp3_stereo, **kwargs)

    # Convert to 16KHZ wav pcm_s16le stereo to mono
    kwargs = {'sampling_rate': 16000, 'out_fmt': 'wav',
                 'out_encoding': 'pcm_s16le', 'to_mono': True,
              'run_validate': True, 'raise_error': True,
              'write_meta': True, 'out_root':'test_output' }
    standardize(wav_stereo, **kwargs)
    standardize(flac_stereo, **kwargs)

    # Convert to 16KHZ flac with compression_level=5
    kwargs = {'sampling_rate': 16000, 'out_fmt': 'flac',
              'out_encoding': 'flac', 'compression_level': 5,
              'run_validate': True, 'raise_error': True,
              'write_meta': True, 'out_root':'test_output' }
    standardize(wav_stereo, **kwargs)
    standardize(mp3_mono, **kwargs)

def hash_file(file_path):
    """
    Returns the SHA-256 hash of a file
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_audio_segment(audio_segment):
    """
    Returns the SHA-256 hash of a pydub.AudioSegment
    """
    sample_bytes = audio_segment.get_array_of_samples().tobytes()
    return hashlib.sha256(sample_bytes).hexdigest()

def walk(audio_type, directory_path):
    """
    Recursively fetches all file paths from a given directory and stores them in a dictionary,
    with the file name as the key and the full path as the value.
    """
    file_map = {}

    for root, _, files in os.walk(directory_path):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), start=directory_path)
            file_map[f'{audio_type}/{relative_path}'] = os.path.join(root, file)
    return file_map

def map_files(audio_type, original_dir, test_dir):
    """
    Walks each directory and matches test files to original files based on their names.
    Returns a dictionary with file names as keys and a tuple of paths (generated, sample) as values.
    """
    # Get all files in both directories
    original_files = walk(audio_type, original_dir)
    test_files = walk(audio_type, test_dir)

    # Create a mapping of matching files
    matched_files = {}

    for file, test_outpath in test_files.items():
        if file in original_files:
            if os.path.splitext(file)[1] in ['.csv', '.json']:
                continue
            matched_files[file] = (original_files[file], test_outpath)
    return matched_files

def validate_files():
    """
    Compare original sample output files with generated files using sha256
    Outputs a csv with comparison details
    """
    mapped_dict = {}
    for audio_type in ['flac', 'm4a', 'mp3', 'wav']:
        test_dir = f'../sample_audio/{audio_type}/test_output'
        original_dir = f'../sample_audio/{audio_type}/pydub'
        mapped_dict.update(map_files(audio_type, original_dir, test_dir))
    summary = [['sample_input', 'original_output', 'test_output', 'original_output_hash',
                 'test_output_hash', 'output_hashes_match', 'original_audio_hash',
                 'test_audio_hash', 'audio_hash_match']]

    hash_matches = {'match': 0,
                    'no match': 0,
                    'audio-only match': 0,
                    'audio-only no match': 0
                    }
    for file, (original_output, test_output) in mapped_dict.items():
        try:
            ## Hash comparison
            original_hash = hash_file(original_output)
            test_hash = hash_file(test_output)
            hash_match = int(original_hash == test_hash)

            if hash_match == 1:
                hash_matches['match'] += 1
            else:
                hash_matches['no match'] +=1

            ## Audio hash only comparison
            original_audio_hash = hash_audio_segment(AudioSegment.from_file(original_output))
            test_audio_hash = hash_audio_segment(AudioSegment.from_file(test_output))
            audio_hash_match = int(original_audio_hash == test_audio_hash)

            if audio_hash_match == 1:
                hash_matches['audio-only match'] += 1
            else:
                hash_matches['audio-only no match'] +=1

            ## Append comparison results
            audio_type = file.split('/')[0]
            sample_input = f'{os.path.basename(file).split(".")[0]}.{audio_type}'
            summary.append([sample_input, original_output, test_output,
                                original_hash, test_hash, hash_match,
                                original_audio_hash, test_audio_hash,
                                audio_hash_match])
        except Exception as error:
            print(f'Error processing {file}: {error}')

    outpath = os.path.join('../sample_audio', 'test_comparison.csv')
    with open(outpath, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(summary)
    print(f'Summary: {hash_matches}')
    print(f'Please see validation CSV written to {outpath} for more details.')

if __name__ == '__main__':
    # generate_comparison_files()
    validate_files()
