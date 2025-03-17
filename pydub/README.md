# Voice Standardize: pydub

This repository contains scripts that show examples of how to use [pydub](https://github.com/jiaaro/pydub) to standardize digital voice audio files with varying metadata to a standard format.

## Installation

Check your Python version:
```sh
python --version
```
Install requirements for Python 3.9.6:
```sh
pip install -r py3-9-6__requirements.txt
```
Install requirements for Python 3.13.1:
```sh
pip install -r py3-13-1__requirements.txt
```
If you do not have the supported Python version installed, you may run the following installation:
```sh
pip install pydub
```

### FFmpeg Setup
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
1. Download [FFmpeg's package for Windows](https://www.ffmpeg.org/download.html#build-windows)
2. Locate the download location of the ZIP file and extract to your desired destination (site-packages)
3. Edit you Environment Variables (Win + S). Click on path > Edit > New and enter the path to \bin in the extracted FFmpeg folder.
4. Verify your installation with the command
   ```sh
   ffmpeg -version
   ```
Please see [Audacity's Installing FFmpeg instructions](https://support.audacityteam.org/basics/installing-ffmpeg) for more details on installing FFmpeg on a Windows machine.


## Standardizing Voice Files
See `run_standardize.main()` for usage examples utilizing audio files in the `../sample_audio` directory. The `pydub_standardize.standardize()` function takes in an input audio filepath (`audio_fp`) and a set of keyword arguments. The keyword arguments include:

| Keyword Argument | Type | Description | Default Value| 
| - | - | - | - |
| sampling_rate | int | The desired sampling rate. | 16000 |
| out_fmt | str | The desired filetype. | wav |
| out_encoding | str | The desired encoding. | pcm_s16le |
| out_ffmpeg_kw | dict | A dictionary of additional ffmpeg parameters to be called. | {} (empty) |
| to_mono | bool | Convert stereo to mono. | False |
| run_validate | bool | Run check on expected versus actual metadata. | False |
| raise_error | bool | Raise an assertion error if expected and actual metadata doesn't match. | False |

## Usage Example

The `run_standardize.py` script generates the below, adjusting to a sampling rate of 16KHz, .WAV file, and pcm_s16le encoding. It also includes converting stereo audio files to mono.

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

You can see several examples in `run_standardize.main()`.

### Sample Input and Output Files and Metadata
Several sample audio files with varying formats and metadata. Each audio file's metadata is captured in a JSON and CSV file. For audio files that were generated via examples here, the parameters and functions used are also included in the metadata files. The functions used to generate the metadata files can be found in `metadata.py` and example usage can be seen in `run_metadata.py`.

```
sample_audio
 |-- flac
 | |-- first_ten_Sample_HV_Clip.flac
 | |-- mono_first_ten_Sample_HV_Clip.flac
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- mono_first_ten_Sample_HV_Clip.wav
 | | |-- ar_16000_c-a_pcm_s16le_ac_1
 | | | |-- first_ten_Sample_HV_Clip.wav
 |-- m4a
 | |-- mono_zoom_audio.m4a
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- mono_zoom_audio.wav
 | | | |-- sample_zoom_audio.wav
 | |-- sample_zoom_audio.m4a
 |-- mp3
 | |-- common_voice_en_21635524.mp3
 | |-- first_ten_Sample_HV_Clip.mp3
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- common_voice_en_21635524.wav
 | | | |-- first_ten_Sample_HV_Clip.wav
 | | |-- ar_16000_c-a_pcm_s16le_ac_1
 | | | |-- first_ten_Sample_HV_Clip.wav
 |-- wav
 | |-- first_ten_Sample_HV_Clip.wav
 | |-- mono_first_ten_Sample_HV_Clip.wav
 | |-- pydub
 | | |-- ar_16000_c-a_pcm_s16le
 | | | |-- first_ten_Sample_HV_Clip.wav
 | | | |-- mono_first_ten_Sample_HV_Clip.wav
 | | |-- ar_16000_c-a_pcm_s16le_ac_1
 | | | |-- first_ten_Sample_HV_Clip.wav
```

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
