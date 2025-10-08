# Windows, Python 3.13.1
## ffmpeg version
```
ffmpeg version N-118350-ge20ee9f9ae-20250123 Copyright (c) 2000-2025 the FFmpeg developers
built with gcc 14.2.0 (crosstool-NG 1.26.0.120_4d36f27)
configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --enable-shared --disable-static --disable-w32threads --enable-pthreads --enable-iconv --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-libxml2 --enable-lzma --enable-fontconfig --enable-libharfbuzz --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --enable-libdavs2 --enable-libdvdread --enable-libdvdnav --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libaribcaption --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp --enable-libzmq --enable-lv2 --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --disable-libvvenc --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-libs=-lgomp --extra-ldflags=-pthread --extra-ldexeflags= --cc=x86_64-w64-mingw32-gcc --cxx=x86_64-w64-mingw32-g++ --ar=x86_64-w64-mingw32-gcc-ar --ranlib=x86_64-w64-mingw32-gcc-ranlib --nm=x86_64-w64-mingw32-gcc-nm --extra-version=20250123
libavutil      59. 55.100 / 59. 55.100
libavcodec     61. 31.101 / 61. 31.101
libavformat    61.  9.106 / 61.  9.106
libavdevice    61.  4.100 / 61.  4.100
libavfilter    10.  6.101 / 10.  6.101
libswscale      8. 13.100 /  8. 13.100
libswresample   5.  4.100 /  5.  4.100
libpostproc    58.  4.100 / 58.  4.100
```
## run_validate.py
```
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
Please see validation CSV written to ../sample_audio\test_comparison.csv for more details.
```
