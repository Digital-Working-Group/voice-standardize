# Debian via Docker, Python 3.13.1
## ffmpeg version
```sh
ffmpeg version 6.1.1 Copyright (c) 2000-2023 the FFmpeg developers
built with gcc 11.2.0 (Anaconda gcc)
configuration: --prefix=/opt/conda --cc=/croot/ffmpeg_1743153284778/_build_env/bin/x86_64-conda-linux-gnu-cc --ar=/croot/ffmpeg_1743153284778/_build_env/bin/x86_64-conda-linux-gnu-ar --nm=/croot/ffmpeg_1743153284778/_build_env/bin/x86_64-conda-linux-gnu-nm --ranlib=/croot/ffmpeg_1743153284778/_build_env/bin/x86_64-conda-linux-gnu-ranlib --strip=/croot/ffmpeg_1743153284778/_build_env/bin/x86_64-conda-linux-gnu-strip --disable-doc --enable-swresample --enable-swscale --enable-openssl --enable-libxml2 --enable-libtheora --enable-demuxer=dash --enable-postproc --enable-hardcoded-tables --enable-libfreetype --enable-libharfbuzz --enable-libfontconfig --enable-libdav1d --enable-zlib --enable-libaom --enable-pic --enable-shared --disable-static --disable-gpl --enable-version3 --disable-sdl2 --enable-libopenh264 --enable-libopus --enable-libmp3lame --enable-libopenjpeg --enable-libvorbis --enable-pthreads --enable-libtesseract --enable-libvpx
libavutil      58. 29.100 / 58. 29.100
libavcodec     60. 31.102 / 60. 31.102
libavformat    60. 16.100 / 60. 16.100
libavdevice    60.  3.100 / 60.  3.100
libavfilter     9. 12.100 /  9. 12.100
libswscale      7.  5.100 /  7.  5.100
libswresample   4. 12.100 /  4. 12.100
```
## run_validate.py
```sh
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.json
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.csv
See ../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.json
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.csv
See ../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.json
../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.csv
See ../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le/mono_first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/mono_zoom_audio.json
../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/mono_zoom_audio.csv
See ../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/mono_zoom_audio.wav for the standardized audio file.
../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/sample_zoom_audio.json
../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/sample_zoom_audio.csv
See ../sample_audio/m4a/test_output/ar_16000_c-a_pcm_s16le/sample_zoom_audio.wav for the standardized audio file.
../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/common_voice_en_21635524.json
../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/common_voice_en_21635524.csv
See ../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/common_voice_en_21635524.wav for the standardized audio file.
../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.json
../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.csv
See ../sample_audio/mp3/test_output/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.json
../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.csv
See ../sample_audio/wav/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.json
../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.csv
See ../sample_audio/flac/test_output/ar_16000_c-a_pcm_s16le_ac_1/first_ten_Sample_HV_Clip.wav for the standardized audio file.
../sample_audio/wav/test_output/ar_16000_c-a_flac_compression_level_5/first_ten_Sample_HV_Clip.json
../sample_audio/wav/test_output/ar_16000_c-a_flac_compression_level_5/first_ten_Sample_HV_Clip.csv
See ../sample_audio/wav/test_output/ar_16000_c-a_flac_compression_level_5/first_ten_Sample_HV_Clip.flac for the standardized audio file.
../sample_audio/mp3/test_output/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.json
../sample_audio/mp3/test_output/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.csv
See ../sample_audio/mp3/test_output/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.flac for the standardized audio file.
Summary: {'match': 0, 'no match': 11, 'audio-only match': 11, 'audio-only no match': 0}
Please see validation CSV written to ../sample_audio/test_comparison.csv for more details.
```