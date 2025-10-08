# Voice Standardize: pydub

This repository contains scripts that show examples of how to use [pydub](https://github.com/jiaaro/pydub) to standardize digital voice audio files with varying metadata to a standard format. The scripts can be run without [Docker](https://docs.docker.com/engine/install/) or with it.

## Installation and Setup

### Python Requirements
```
pydub
   |-- requirements
   |   |-- py3-13-1
   |   |   |-- Dockerfile
   |   |   |-- build_docker.sh
   |   |   |-- pip-licenses.md
   |   |   |-- requirements.txt
   |   |   |-- run_docker.sh
   |   |   |-- validate_docker.md
   |   |   |-- validate_windows.md
   |   |-- py3-9-6
   |   |   |-- Dockerfile
   |   |   |-- build_docker.sh
   |   |   |-- pip-licenses.md
   |   |   |-- requirements.txt
   |   |   |-- run_docker.sh
   |   |   |-- validate_docker.md
   |   |   |-- validate_windows.md
```

Check your Python version:
```sh
python --version
```
See [Anaconda](https://www.anaconda.com/download/success) as an option to switch between Python versions. This repository has been tested with Python 3.10.11.

Install requirements for Python 3.9.6:
```sh
pip install -r requirements/py3-9-6/requirements.txt 
```

Install requirements for Python 3.13.1:
```sh
pip install -r requirements/py3-13-1/requirements.txt 
```

Note: you may use the pip install command described above even if you are working with a different Python version, but you may need to adjust the requirements.txt file to fit any dependencies specific to that Python version.

### Requirements.txt License Information
License information for each set of requirements.txt can be found in their respective `pip-licenses.md` file within the requirements/python[version] folders.

### Docker Support
[Docker](https://docs.docker.com/engine/install/) support can be found via the `Dockerfile` and `build_docker.sh` and `run_docker.sh` files.

Please see Docker's documentation for more information ([docker build](https://docs.docker.com/build/), [Dockerfile](https://docs.docker.com/build/concepts/dockerfile/), [docker run](https://docs.docker.com/reference/cli/docker/container/run/)).

### FFmpeg Setup
If utilizing Docker, FFmpeg is already installed within the Docker environment.

The following instructions have been taken from [pydub's documentation](http://github.com/jiaaro/pydub?tab=readme-ov-file#getting-ffmpeg-set-up)

> ### Mac (using homebrew):
> 
> #### libav
> brew install libav
> 
> ####    OR    #####
> 
> #### ffmpeg
> brew install ffmpeg
>
> ### Linux (using aptitude):
> 
> #### libav
> apt-get install libav-tools libavcodec-extra
> 
> ####    OR    #####
> 
> #### ffmpeg
> apt-get install ffmpeg libavcodec-extra
>

Windows FFmpeg installation:
1. Download [FFmpeg's package for Windows](https://www.ffmpeg.org/download.html#build-windows).
2. Locate the download location of the ZIP file and extract to your desired destination.
3. Edit your Environment Variables (Windows Key -> Edit environment variables for your account). Edit Path -> New -> Enter the path to \bin in the extracted FFmpeg folder.
4. Verify your installation with the command
   ```sh
   ffmpeg -version
   ```
Please see a few other tutorials on this process for Windows. Note that you may prefer to edit the environment variables for your account and not for the whole system, as shown in some tutorials.
1. [Audacity](https://support.audacityteam.org/basics/installing-ffmpeg).
2. [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
3. [Transloadit](https://transloadit.com/devtips/how-to-install-ffmpeg-on-windows-a-complete-guide/).

### FFmpeg Version
Please see the exact FFmpeg version used in this repository ([2025-02-24-git-6232f416b1-full_build](https://github.com/GyanD/codexffmpeg/releases/tag/2025-02-24-git-6232f416b1)):

```sh
ffmpeg version 2025-02-24-git-6232f416b1-full_build-www.gyan.dev Copyright (c) 2000-2025 the FFmpeg developers
  built with gcc 14.2.0 (Rev1, Built by MSYS2 project)
  configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-fontconfig --enable-iconv --enable-gnutls --enable-lcms2 --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-libsnappy --enable-zlib --enable-librist --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-libbluray --enable-libcaca --enable-libdvdnav --enable-libdvdread --enable-sdl2 --enable-libaribb24 --enable-libaribcaption --enable-libdav1d --enable-libdavs2 --enable-libopenjpeg --enable-libquirc --enable-libuavs3d --enable-libxevd --enable-libzvbi --enable-libqrencode --enable-librav1e --enable-libsvtav1 --enable-libvvenc --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxeve --enable-libxvid --enable-libaom --enable-libjxl --enable-libvpx --enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-libgme --enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine --enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libcodec2 --enable-libilbc --enable-libgsm --enable-liblc3 --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b --enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint
  libavutil      59. 57.100 / 59. 57.100
  libavcodec     61. 33.102 / 61. 33.102
  libavformat    61.  9.107 / 61.  9.107
  libavdevice    61.  4.100 / 61.  4.100
  libavfilter    10.  9.100 / 10.  9.100
  libswscale      8. 13.100 /  8. 13.100
  libswresample   5.  4.100 /  5.  4.100
  libpostproc    58.  4.100 / 58.  4.100
Universal media converter
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...
```

## Jupyter Notebook Examples
Please run [jupyter notebook](https://docs.jupyter.org/en/latest/running.html) and see [voice_standardize_examples.ipynb](voice_standardize_examples.ipynb) for an interactive set of examples. Also, see the usage example sections below.

## Standardizing Voice Files
See `run_standardize.main()` for usage examples utilizing audio files in the `../sample_audio` directory. The `pydub_standardize.standardize()` function takes in an input audio filepath (`audio_fp`) and a set of keyword arguments:

| Keyword Argument | Type | Description | Default Value| 
| - | - | - | - |
| sampling_rate | int | The desired sampling rate. | 16000 |
| out_fmt | str | The desired filetype. | wav |
| out_encoding | str | The desired encoding. | pcm_s16le |
| out_ffmpeg_kw | dict | A dictionary of additional ffmpeg parameters to be called. | {} (empty) |
| to_mono | bool | Convert stereo to mono. | False |
| run_validate | bool | Run check on expected versus actual metadata. | False |
| raise_error | bool | Raise an assertion error if expected and actual metadata doesn't match. | False |
| write_meta | bool | Writes metadata to JSON and CSV files. | False |

## Usage Example

The `run_standardize.py` script can be run using the format below.
```python
from pydub_standardize import standardize
standardize(YOUR_AUDIO_FILEPATH, OPTIONAL_KWARGS)
```
For instance, you could run:
```python
from pydub_standardize import standardize
kwargs = {'sampling_rate': 16000, 'out_fmt': 'wav', 
              'out_encoding': 'pcm_s16le', 'run_validate': True,
              'raise_error': True}
standardize('../sample_audio/flac/first_ten_Sample_HV_Clip.flac', **kwargs)
```
This would output a .WAV file standardized to have a sampling rate of 16KHz (`sampling_rate`) and pcm_s16le (`out_encoding`) encoding. The metadata of the output file will be validated versus the input parameters (`run_validate`) and an AssertionError will be raised if they don't match (`raise_error`).

`run_validate=True` checks channels (ac), sample_rate (ar), codec_name (c:a), see map_keys in `pydub_standardize.validate_metadata()` and writes `validate_{filename}.csv` in the same directory as the output audio file.

For a different example, you could run:
```python
from pydub_standardize import standardize
wav_stereo = '../sample_audio/wav/first_ten_Sample_HV_Clip.wav'
kwargs = {'sampling_rate': 16000, 'out_fmt': 'wav', 
          'out_encoding': 'pcm_s16le', 'to_mono': True,
          'run_validate': True, 'raise_error': True,
          'write_meta': True }
standardize(wav_stereo, **kwargs)
```
This would output a .WAV file standardized to have a sampling rate of 16KHz (`sampling_rate`), pcm_s16le (`out_encoding`) encoding and converted to a single channel (`to_mono`). The metadata of the output file will be validated versus the input parameters (`run_validate`) and an AssertionError will be raised if they don't match (`raise_error`). It would also write a JSON and CSV file recording the metadata (`write_meta`).

You can see several examples in `run_standardize.main()`.

### Sample Input and Output Files and Metadata
This repository provides several sample audio files with varying formats and metadata. Each audio file's metadata is captured in a JSON and CSV file. For audio files that were generated via examples here, the parameters and functions used are also included in the metadata files. The functions used to generate the metadata files can be found in `metadata.py` and example usage can be seen in `run_metadata.py`.

```
sample_audio
 |-- flac
 | |-- first_ten_Sample_HV_Clip.csv
 | |-- first_ten_Sample_HV_Clip.flac
 | |-- first_ten_Sample_HV_Clip.json
 | |-- mono_first_ten_Sample_HV_Clip.csv
 | |-- mono_first_ten_Sample_HV_Clip.flac
 | |-- mono_first_ten_Sample_HV_Clip.json
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- mono_first_ten_Sample_HV_Clip.csv
 | | | |-- mono_first_ten_Sample_HV_Clip.json
 | | | |-- mono_first_ten_Sample_HV_Clip.wav
 | | |-- ar_16000_c-a_pcm_s16le_ac_1
 | | | |-- first_ten_Sample_HV_Clip.csv
 | | | |-- first_ten_Sample_HV_Clip.json
 | | | |-- first_ten_Sample_HV_Clip.wav
 |-- m4a
 | |-- mono_zoom_audio.csv
 | |-- mono_zoom_audio.json
 | |-- mono_zoom_audio.m4a
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- mono_zoom_audio.csv
 | | | |-- mono_zoom_audio.json
 | | | |-- mono_zoom_audio.wav
 | | | |-- sample_zoom_audio.csv
 | | | |-- sample_zoom_audio.json
 | | | |-- sample_zoom_audio.wav
 | |-- sample_zoom_audio.csv
 | |-- sample_zoom_audio.json
 | |-- sample_zoom_audio.m4a
 |-- mp3
 | |-- common_voice_en_21635524.csv
 | |-- common_voice_en_21635524.json
 | |-- common_voice_en_21635524.mp3
 | |-- first_ten_Sample_HV_Clip.csv
 | |-- first_ten_Sample_HV_Clip.json
 | |-- first_ten_Sample_HV_Clip.mp3
 | |-- pydub
 | | |-- ar_16000_c-a_flac_compression_level_5
 | | | |-- common_voice_en_21635524.csv
 | | | |-- common_voice_en_21635524.flac
 | | | |-- common_voice_en_21635524.json
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- common_voice_en_21635524.csv
 | | | |-- common_voice_en_21635524.json
 | | | |-- common_voice_en_21635524.wav
 | | | |-- first_ten_Sample_HV_Clip.csv
 | | | |-- first_ten_Sample_HV_Clip.json
 | | | |-- first_ten_Sample_HV_Clip.wav
 |-- wav
 | |-- first_ten_Sample_HV_Clip.csv
 | |-- first_ten_Sample_HV_Clip.json
 | |-- first_ten_Sample_HV_Clip.wav
 | |-- mono_first_ten_Sample_HV_Clip.csv
 | |-- mono_first_ten_Sample_HV_Clip.json
 | |-- mono_first_ten_Sample_HV_Clip.wav
 | |-- pydub
 | | |-- ar_16000_c-a_flac_compression_level_5
 | | | |-- first_ten_Sample_HV_Clip.csv
 | | | |-- first_ten_Sample_HV_Clip.flac
 | | | |-- first_ten_Sample_HV_Clip.json
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- first_ten_Sample_HV_Clip.csv
 | | | |-- first_ten_Sample_HV_Clip.json
 | | | |-- first_ten_Sample_HV_Clip.wav
 | | | |-- mono_first_ten_Sample_HV_Clip.csv
 | | | |-- mono_first_ten_Sample_HV_Clip.json
 | | | |-- mono_first_ten_Sample_HV_Clip.wav
 | | |-- ar_16000_c-a_pcm_s16le_ac_1
 | | | |-- first_ten_Sample_HV_Clip.csv
 | | | |-- first_ten_Sample_HV_Clip.json
 | | | |-- first_ten_Sample_HV_Clip.wav
```

### [sample_audio/mp3/common_voice_en_21635524.json](../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.json)
```json
{
    "streams": [
        {
            "index": 0,
            "codec_name": "flac",
            "codec_long_name": "FLAC (Free Lossless Audio Codec)",
            "codec_type": "audio",
            "codec_tag_string": "[0][0][0][0]",
            "codec_tag": "0x0000",
            "sample_fmt": "s16",
            "sample_rate": "16000",
            "channels": 1,
            "channel_layout": "mono",
            "bits_per_sample": 16,
            "initial_padding": 0,
            "r_frame_rate": "0/0",
            "avg_frame_rate": "0/0",
            "time_base": "1/16000",
            "start_pts": 0,
            "start_time": "0.000000",
            "duration_ts": 104064,
            "duration": "6.504000",
            "bits_per_raw_sample": "16",
            "extradata_size": 34,
            "disposition": {
                "default": 0,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0,
                "timed_thumbnails": 0,
                "non_diegetic": 0,
                "captions": 0,
                "descriptions": 0,
                "metadata": 0,
                "dependent": 0,
                "still_image": 0,
                "multilayer": 0
            }
        }
    ],
    "format": {
        "filename": "../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.flac",
        "nb_streams": 1,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "flac",
        "format_long_name": "raw FLAC",
        "start_time": "0.000000",
        "duration": "6.504000",
        "size": "105460",
        "bit_rate": "129717",
        "probe_score": 100,
        "tags": {
            "encoder": "Lavf61.9.107"
        }
    },
    "ffmpeg_command": "ffmpeg -i '../sample_audio/mp3/common_voice_en_21635524.mp3' -ar 16000 -c:a flac -compression_level 5 '../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.flac'",
    "pydub_command": "export('../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.flac', format=flac, parameters=['-ar', '16000', '-c:a', 'flac', '-compression_level', '5'])"
}
```

### [sample_audio/mp3/common_voice_en_21635524.csv](../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.csv)
```csv
index,codec_name,codec_long_name,codec_type,codec_tag_string,codec_tag,sample_fmt,sample_rate,channels,channel_layout,bits_per_sample,initial_padding,r_frame_rate,avg_frame_rate,time_base,start_pts,start_time,duration_ts,duration,bits_per_raw_sample,extradata_size,disposition.default,disposition.dub,disposition.original,disposition.comment,disposition.lyrics,disposition.karaoke,disposition.forced,disposition.hearing_impaired,disposition.visual_impaired,disposition.clean_effects,disposition.attached_pic,disposition.timed_thumbnails,disposition.non_diegetic,disposition.captions,disposition.descriptions,disposition.metadata,disposition.dependent,disposition.still_image,disposition.multilayer,format.filename,format.nb_streams,format.nb_programs,format.nb_stream_groups,format.format_name,format.format_long_name,format.start_time,format.duration,format.size,format.bit_rate,format.probe_score,format.tags.encoder
0,flac,FLAC (Free Lossless Audio Codec),audio,[0][0][0][0],0x0000,s16,16000,1,mono,16,0,0/0,0/0,1/16000,0,0.000000,104064,6.504000,16,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,../sample_audio/mp3/pydub/ar_16000_c-a_flac_compression_level_5/common_voice_en_21635524.flac,1,0,0,flac,raw FLAC,0.000000,6.504000,105460,129717,100,Lavf61.9.107
```
### [sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.json](../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.json)
```json
{
    "streams": [
        {
            "index": 0,
            "codec_name": "pcm_s16le",
            "codec_long_name": "PCM signed 16-bit little-endian",
            "codec_type": "audio",
            "codec_tag_string": "[1][0][0][0]",
            "codec_tag": "0x0001",
            "sample_fmt": "s16",
            "sample_rate": "16000",
            "channels": 2,
            "bits_per_sample": 16,
            "initial_padding": 0,
            "r_frame_rate": "0/0",
            "avg_frame_rate": "0/0",
            "time_base": "1/16000",
            "duration_ts": 160000,
            "duration": "10.000000",
            "bit_rate": "512000",
            "disposition": {
                "default": 0,
                "dub": 0,
                "original": 0,
                "comment": 0,
                "lyrics": 0,
                "karaoke": 0,
                "forced": 0,
                "hearing_impaired": 0,
                "visual_impaired": 0,
                "clean_effects": 0,
                "attached_pic": 0,
                "timed_thumbnails": 0,
                "non_diegetic": 0,
                "captions": 0,
                "descriptions": 0,
                "metadata": 0,
                "dependent": 0,
                "still_image": 0,
                "multilayer": 0
            },
            "bits_per_raw_sample": 16
        }
    ],
    "format": {
        "filename": "../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav",
        "nb_streams": 1,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "wav",
        "format_long_name": "WAV / WAVE (Waveform Audio)",
        "duration": "10.000000",
        "size": "640078",
        "bit_rate": "512062",
        "probe_score": 99,
        "tags": {
            "encoder": "Lavf61.9.107"
        }
    },
    "ffmpeg_command": "ffmpeg -i '../sample_audio/wav/first_ten_Sample_HV_Clip.wav' -ar 16000 -c:a pcm_s16le '../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav'",
    "pydub_command": "export('../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav', format=wav, parameters=['-ar', '16000', '-c:a', 'pcm_s16le'])"
}
```

### [sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.csv](../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.csv)
```csv
index,codec_name,codec_long_name,codec_type,codec_tag_string,codec_tag,sample_fmt,sample_rate,channels,bits_per_sample,initial_padding,r_frame_rate,avg_frame_rate,time_base,duration_ts,duration,bit_rate,disposition.default,disposition.dub,disposition.original,disposition.comment,disposition.lyrics,disposition.karaoke,disposition.forced,disposition.hearing_impaired,disposition.visual_impaired,disposition.clean_effects,disposition.attached_pic,disposition.timed_thumbnails,disposition.non_diegetic,disposition.captions,disposition.descriptions,disposition.metadata,disposition.dependent,disposition.still_image,disposition.multilayer,bits_per_raw_sample,format.filename,format.nb_streams,format.nb_programs,format.nb_stream_groups,format.format_name,format.format_long_name,format.duration,format.size,format.bit_rate,format.probe_score,format.tags.encoder
0,pcm_s16le,PCM signed 16-bit little-endian,audio,[1][0][0][0],0x0001,s16,16000,2,16,0,0/0,0/0,1/16000,160000,10.000000,512000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,../sample_audio/wav/pydub/ar_16000_c-a_pcm_s16le/first_ten_Sample_HV_Clip.wav,1,0,0,wav,WAV / WAVE (Waveform Audio),10.000000,640078,512062,99,Lavf61.9.107
```

## Generating metadata for existing files
See `run_metadata.main()` for usage examples utilizing the scripts in `metadata.py` to generate metadata for exisiting files. If you wish to include the FFmpeg and pydub commands that would be used to create these files, you must pass in either the components or the command as key word arguments when calling `metadata.write_metadata()`.

### Usage Example
The `run_metadata.py` script can be run using the format below.
```python
from metadata import write_metadata
write_metadata(YOUR_AUDIO_FILEPATH, OPTIONAL_KWARGS)
```

For instance, you could run:
```python
from metadata import write_metadata
flac_mono = '../sample_audio/flac/mono_first_ten_Sample_HV_Clip.flac'
kwargs = {'append_json_dict':{'ffmpeg_command': f"ffmpeg -i '{wav_mono}' -compression_level 5 -af aformat=s16:44100 ' {flac_mono}'"}}
write_metadata(flac_mono, **kwargs)
```
This would output JSON and CSV files that capture the metadata for the file specified, appending the FFmpeg command used to create the file and the equivalent pydub command to the end of the JSON.

You can see several examples in `run_metadata.main()`.

## Supported Input and Output Types
This repository depends on `pydub.AudioSegment.from_file()` to read input files, which uses [ffmpeg](https://www.ffmpeg.org/) or avconv (from [libav](https://github.com/libav/libav)) in the background. Those input file types include at least WAV, raw, PCM, MP3, FLV, and OGG (see [audio_segment.from_file()](https://github.com/jiaaro/pydub/blob/master/pydub/audio_segment.py)).

Similarly, this repository depends on `pydub.AudioSegment.export()` to write output files, which also uses ffmpeg or avconv in the background. These output file types include at least MP3, WAV, raw, OGG, or other ffmpeg/avconv supported files (see [audio_segment.export()](https://github.com/jiaaro/pydub/blob/master/pydub/audio_segment.py)).

This repository includes test input audio files of the following formats (FLAC, m4a, mp3, WAV) and includes test output audio files of the following formats (WAV, FLAC).

## Validation
The scripts provided in `validate.py` allow you to check output extracted on your machine using the sample input files against the provided sample output. To perform the validation check, see `run_validate.py`:
```python
from validate import generate_comparison_files, validate_files

if __name__ == '__main__':
    generate_comparison_files()
    validate_files()
```

This will output standardized audio to ../sample_audio/*FILETYPE*/test_output and will output a comparison CSV to ../sample_audio. The comparison CSV has the following columns:

| Column | Description | Example | 
| - | - | - |
| sample_input | Filepath to the source audio file. | first_ten_Sample_HV_Clip.wav |
| original_output | Filepath to the original output data, pre-generated on the repository. | ../sample_audio/wav/pydub\ar_16000_c-a_flac_compression_level_5\first_ten_Sample_HV_Clip.flac |
| test_output | Filepath to the test_output data, generated from the source audio file, but via the user's machine. | ../sample_audio/wav/test_output\ar_16000_c-a_flac_compression_level_5\first_ten_Sample_HV_Clip.flac |
| original_output_hash | sha256 hash generated on original_output. | 4d6... |
| test_output_hash | sha256 hash generated on test_output. | 4d6... |
| output_hashes_match | Indicates whether original_output_hash and test_output_hash are equal (1) or not (0) | 1 |
| original_audio_hash | sha256 hash generated on AudioSegment of original_output. | 698... |
| test_audio_hash | sha256 hash generated on AudioSegment of test_output. | 698... |
| audio_hashes_match | Indicates whether original_audio_hash and test_audio_hash are equal (1) or not (0) | 1 |

 The validation uses sha256 hashes and only compares the output audio files. *Original_hash, test_hash* and *hash_comparison* all record the results from looking at the entire audio file, including metadata.

Generating files using different versions of FFmpeg may affect the results (e.g., metadata such as the libavformat version) so please see *original_audio_hash, test_audio_hash* and *audio_hash_comparison* to compare only the audio segement.

The metadata CSV and JSON files are excluded from these checks, since the audio filepaths will always differ.

Please see the `validate_<docker/windows>.md` files in the respective `requirements/py<version>/` folders for the expected run_validate.py output.

## Citations
```bibtex
@inproceedings{commonvoice:2020,
  author = {Ardila, R. and Branson, M. and Davis, K. and Henretty, M. and Kohler, M. and Meyer, J. and Morais, R. and Saunders, L. and Tyers, F. M. and Weber, G.},
  title = {Common Voice: A Massively-Multilingual Speech Corpus},
  booktitle = {Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)},
  pages = {4211--4215},
  year = 2020
}
```
