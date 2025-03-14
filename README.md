# Voice Standardize
This repository contains example workflows, READMEs, sample data, and [Docker](https://www.docker.com/) files that facilitate the usage of various open-source voice feature extraction packages, tools, and datasets for standardizing digital voice audio files.

It is a part of a larger [toolkit](https://github.com/FHS-BAP/Voice-Feature-Extraction-Toolkit/) that was developed to support scientific research surrounding investigations of relationships between brain aging and voice features, although the extraction of voice features does have wider applicability. We invite others to please offer their questions, ideas, feedback, and improvements on this repository.

## Overview
| Name | Description |
| - | - |
| **pydub** | Standardize digital voice audio files with varying metadata to a standard format using [pydub](https://github.com/jiaaro/pydub).

## Sample Input Files
```
sample_audio
 |-- flac
 | |-- first_ten_Sample_HV_Clip.flac
 | |-- mono_first_ten_Sample_HV_Clip.flac
 |-- m4a
 | |-- mono_zoom_audio.m4a
 | |-- sample_zoom_audio.m4a
 |-- mp3
 | |-- common_voice_en_21635524.mp3
 | |-- first_ten_Sample_HV_Clip.mp3
 |-- wav
 | |-- first_ten_Sample_HV_Clip.wav
 | |-- mono_first_ten_Sample_HV_Clip.wav
```
| filename | sampling_rate (Hz)| encoding | channels | channel_layout | origin |
| - | - | - | - | - | - |
| first_ten_Sample_HV_Clip.flac | 44100 | Lavf61.9.106 |  2 |stereo | - |
| mono_first_ten_Sample_HV_Clip.flac | 44100 | Lavf61.9.106 | 1 | mono | - |
| mono_zoom_audio.m4a | 48000 | Lavf61.9.106 | 1 | mono | - |
| sample_zoom_audio.m4a | 48000 | AAC (Advanced Audio Coding) | 2 | stereo | - |
| common_voice_en_21635524.mp3 | 48000 | Lavf57.56.101 | 1 | mono |[Common Voice Corpus 13.0](https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0)|
| first_ten_Sample_HV_Clip.mp3 | 44100 | Lavf61.9.106 | 2 | stereo | - |
| first_ten_Sample_HV_Clip.wav | 44100 | Lavf59.16.100 | 2 | unknown | - |
| mono_first_ten_Sample_HV_Clip.wav | 44100 | Lavf61.9.106 | 1 | unknown | - |

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