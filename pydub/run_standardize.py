"""
run_standardize.py
run standardization example
"""
from pydub_standardize import standardize

def mp3_to_wav():
	"""
	convert sample MP3 to 16KHz PCM16_le WAV;
	"""
	audio_fp = '../sample_audio/mp3/common_voice_en_21635524.mp3'
	kwargs = {'sampling_rate': 16000, 'out_fmt': 'wav', 'out_encoding': 'pcm_s16le'}
	standardize(audio_fp, **kwargs)

def main():
	"""
	main entrypoint
	"""
	mp3_to_wav()

if __name__ == '__main__':
	main()
