"""
run_metadata.py
run metadata writing functions + add additional metadata info outside of pydub.utils
"""
from metadata import write_metadata

def main():
    """
    run metadata writing examples
    """
    # All input files in ../sample_audio
    flac_mono = '../sample_audio/flac/mono_first_ten_Sample_HV_Clip.flac'
    flac_stereo = '../sample_audio/flac/first_ten_Sample_HV_Clip.flac'
    mp3_mono = '../sample_audio/mp3/common_voice_en_21635524.mp3'
    mp3_stereo = '../sample_audio/mp3/first_ten_Sample_HV_Clip.mp3'
    m4a_mono = '../sample_audio/m4a/mono_zoom_audio.m4a'
    m4a_stereo = '../sample_audio/m4a/sample_zoom_audio.m4a'
    wav_mono = '../sample_audio/wav/mono_first_ten_Sample_HV_Clip.wav'
    wav_stereo = '../sample_audio/wav/first_ten_Sample_HV_Clip.wav'

    # Generated
    kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{wav_mono}' -compression_level 5 -af aformat=s16:44100 '{flac_mono}'"}}
    write_metadata(flac_mono, **kwargs)
    kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{wav_stereo}' -compression_level 5 -af aformat=s16:44100 '{flac_stereo}'"}}
    write_metadata(flac_stereo)
    kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{wav_stereo}' -ar 44100 -ac 2 '{mp3_stereo}'"}}
    write_metadata(mp3_stereo, **kwargs)
    kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{m4a_stereo}' -ac 1 '{m4a_mono}'"}}
    write_metadata(m4a_mono, **kwargs)
    kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{wav_stereo}' -ar 44100 -ac 1 '{wav_mono}'"}}
    write_metadata(wav_mono, **kwargs)

    ## Non-generated
    write_metadata(wav_stereo)
    write_metadata(m4a_stereo)
    write_metadata(mp3_mono)

if __name__ == '__main__':
    main()
