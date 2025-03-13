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
   |-- mp3
   |   |-- common_voice_en_21635524.mp3
```
| filename | sampling_rate | encoding | channels | origin |
| - | - | - | - | - |
| common_voice_en_21635524.mp3 | 48KHz | Lavf57.56.101 | mono |[Common Voice Corpus 13.0](https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0)|

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