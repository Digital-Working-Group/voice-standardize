"""
metadata.py
get and write metadata
"""
import os
import csv
import json
from pydub.utils import mediainfo_json

def format_json_as_csv(json_dict):
    """
    reformat the JSON to write as a CSV
    """
    metadata_dict = {}
    stream_md = json_dict['streams'][0]
    ## assuming just one stream;
    format_md = json_dict['format']
    metadata_dict = {}
    for stream_k, stream_v in stream_md.items():
        if stream_k == 'disposition':
            for disp_k, disp_v in stream_v.items():
                metadata_dict[f'disposition.{disp_k}'] = disp_v
            continue
        metadata_dict[stream_k] = stream_v
    for format_k, format_v in format_md.items():
        if format_k == 'tags':
            for tag_k, tag_v in format_v.items():
                metadata_dict[f'format.tags.{tag_k}'] = tag_v
            continue
        metadata_dict[f'format.{format_k}'] = format_v
    return metadata_dict

def write_metadata_dict_to_csv(metadata_dict, csv_out):
    """
    write metadata dictionary to CSV
    """
    with open(csv_out, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=metadata_dict.keys())
        writer.writeheader()
        writer.writerow(metadata_dict)

def metadata_json_to_csv(json_dict, csv_out):
    """
    write the metadata json to CSV;
    if the key is a dict, then write as "key.<field>""
    format: {'filename'} -> 'format.filename'
    """
    metadata_dict = format_json_as_csv(json_dict)
    write_metadata_dict_to_csv(metadata_dict, csv_out)

def write_metadata(audio_fp, **kwargs):
    """
    get and write metadata to JSON and CSV;
    append_json_dict: add additional info to the JSON dict as needed;
    """
    append_json_dict = kwargs.get('append_json_dict', {})
    quiet = kwargs.get('quiet', False)
    fp_without_ext = os.path.splitext(audio_fp)[0]
    json_out = f'{fp_without_ext}.json'
    json_dict = mediainfo_json(audio_fp)
    json_dict.update(append_json_dict)
    with open(json_out, 'w') as outfile:
        json.dump(json_dict, outfile, indent=4, sort_keys=False)
    csv_out = f'{fp_without_ext}.csv'
    metadata_json_to_csv(json_dict, csv_out)
    if not quiet:
        print(json_out)
        print(csv_out)
