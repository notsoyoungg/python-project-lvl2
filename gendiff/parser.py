import json
import yaml
from os.path import abspath


def format_dict(dict_):
    for key in dict_:
        if not isinstance(dict_[key], dict):
            dict_[key] = json.dumps(dict_[key])
        if isinstance(dict_[key], dict):
            format_dict(dict_[key])
    return dict_


def parse(content, format):
    if format == 'json':
        data = format_dict(json.load(content))
        return data
    else:
        data = format_dict(yaml.safe_load(content))
        return data


def get_content_and_format(filepath):
    content = open(abspath(filepath))
    if filepath[-4] == 'json':
        return content, 'json'
    else:
        return content, 'yaml'
