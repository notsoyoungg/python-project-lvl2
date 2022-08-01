import json
import yaml
from yaml.loader import FullLoader
from os.path import abspath


def format_dict(dict_):
    for key in dict_:
        if not isinstance(dict_[key], dict):
            dict_[key] = json.dumps(dict_[key])
        if isinstance(dict_[key], dict):
            format_dict(dict_[key])
    return dict_


def get_data(filepath, format):
    if format == 'json':
        data = format_dict(json.load(open_file(filepath)))
        return data
    else:
        data = format_dict(yaml.load(open_file(filepath), FullLoader))
        return data


def open_file(filepath):
    content = open(abspath(filepath))
    return content


def get_format(filepath):
    if filepath[-4] == 'json':
        return 'json'
    else:
        return 'yaml'
