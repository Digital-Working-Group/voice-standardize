# Voice Standardize
This repository contains example workflows, READMEs, sample data, and [Docker](https://www.docker.com/) files that facilitate the usage of various open-source voice feature extraction packages, tools, and datasets for standardizing digital voice audio files.

It is a part of a larger [toolkit](https://github.com/FHS-BAP/Voice-Feature-Extraction-Toolkit/) that was developed to support scientific research surrounding investigations of relationships between brain aging and voice features, although the extraction of voice features does have wider applicability. We invite others to please offer their questions, ideas, feedback, and improvements on this repository.

## Overview
| Name | Description |
| - | - |
| **pydub** | Standardize digital voice audio files with varying metadata to a standard format using [pydub](https://github.com/jiaaro/pydub).

## Sample Input Files and Metadata
Several sample audio files with varying formats and metadata. Each audio file's metadata is captured in a JSON and CSV file. For audio files that were generated via examples here, the parameters and functions used are also included in the metadata files.
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
| filename | sampling_rate (Hz) | origin |
| - | - | - |
| first_ten_Sample_HV_Clip.flac | 44100 | FHS-BAP Sample Data |
| mono_first_ten_Sample_HV_Clip.flac | 44100 | FHS-BAP Sample Data |
| mono_zoom_audio.m4a | 48000 | FHS-BAP Sample Data |
| sample_zoom_audio.m4a | 48000 | FHS-BAP Sample Data |
| common_voice_en_21635524.mp3 | 48000 | [Common Voice Corpus 13.0](https://huggingface.co/datasets/mozilla-foundation/common_voice_13_0)|
| first_ten_Sample_HV_Clip.mp3 | 44100 | FHS-BAP Sample Data |
| first_ten_Sample_HV_Clip.wav | 44100 | FHS-BAP Sample Data |
| mono_first_ten_Sample_HV_Clip.wav | 44100 | FHS-BAP Sample Data |

### sample_audio/mp3/common_voice_en_21635524.json
```json
{
    "streams": [
        {
            "index": 0,
            "codec_name": "mp3",
            "codec_long_name": "MP3 (MPEG audio layer 3)",
            "codec_type": "audio",
            "codec_tag_string": "[0][0][0][0]",
            "codec_tag": "0x0000",
            "sample_fmt": "fltp",
            "sample_rate": "48000",
            "channels": 1,
            "channel_layout": "mono",
            "bits_per_sample": 32,
            "initial_padding": 0,
            "r_frame_rate": "0/0",
            "avg_frame_rate": "0/0",
            "time_base": "1/14112000",
            "start_pts": 0,
            "start_time": "0.000000",
            "duration_ts": 91784448,
            "duration": "6.504000",
            "bit_rate": "64000",
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
            "bits_per_raw_sample": 32
        }
    ],
    "format": {
        "filename": "../sample_audio/mp3/common_voice_en_21635524.mp3",
        "nb_streams": 1,
        "nb_programs": 0,
        "nb_stream_groups": 0,
        "format_name": "mp3",
        "format_long_name": "MP2/3 (MPEG audio layer 2/3)",
        "start_time": "0.000000",
        "duration": "6.504000",
        "size": "52077",
        "bit_rate": "64055",
        "probe_score": 51,
        "tags": {
            "encoder": "Lavf57.56.101"
        }
    }
}
```

### sample_audio/mp3/common_voice_en_21635524.csv
```csv
index,codec_name,codec_long_name,codec_type,codec_tag_string,codec_tag,sample_fmt,sample_rate,channels,channel_layout,bits_per_sample,initial_padding,r_frame_rate,avg_frame_rate,time_base,start_pts,start_time,duration_ts,duration,bit_rate,disposition.default,disposition.dub,disposition.original,disposition.comment,disposition.lyrics,disposition.karaoke,disposition.forced,disposition.hearing_impaired,disposition.visual_impaired,disposition.clean_effects,disposition.attached_pic,disposition.timed_thumbnails,disposition.non_diegetic,disposition.captions,disposition.descriptions,disposition.metadata,disposition.dependent,disposition.still_image,disposition.multilayer,bits_per_raw_sample,format.filename,format.nb_streams,format.nb_programs,format.nb_stream_groups,format.format_name,format.format_long_name,format.start_time,format.duration,format.size,format.bit_rate,format.probe_score,format.tags.encoder
0,mp3,MP3 (MPEG audio layer 3),audio,[0][0][0][0],0x0000,fltp,48000,1,mono,32,0,0/0,0/0,1/14112000,0,0.000000,91784448,6.504000,64000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,../sample_audio/mp3/common_voice_en_21635524.mp3,1,0,0,mp3,MP2/3 (MPEG audio layer 2/3),0.000000,6.504000,52077,64055,51,Lavf57.56.101
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