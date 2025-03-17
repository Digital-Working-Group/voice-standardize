"""
run_metadata.py
run metadata writing functions + add additional metadata info outside of pydub.utils
"""
from metadata import write_metadata

def main():
    """
    run metadata writing examples
    """
    mp3_mono = '../sample_audio/mp3/common_voice_en_21635524.mp3'
    write_metadata(mp3_mono)

if __name__ == '__main__':
    main()
