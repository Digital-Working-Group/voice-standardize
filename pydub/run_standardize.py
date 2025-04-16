"""
run_standardize.py
run standardization example
"""
from pydub_standardize import standardize

def main():
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
              'raise_error': True, 'write_meta': True}
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
              'write_meta': True }
    standardize(wav_stereo, **kwargs)
    standardize(flac_stereo, **kwargs)

    # Convert to 16KHZ flac with compression_level=5
    kwargs = {'sampling_rate': 16000, 'out_fmt': 'flac',
              'out_encoding': 'flac', 'compression_level': 5,
              'run_validate': True, 'raise_error': True,
              'write_meta': True }
    standardize(wav_stereo, **kwargs)
    standardize(mp3_mono, **kwargs)

if __name__ == '__main__':
    main()
