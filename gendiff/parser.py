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


def parse(filepath):
    if filepath[-4] == 'json':
        data = format_dict(json.load(open(abspath(filepath))))
        return data
    else:
        data = format_dict(yaml.load(open(abspath(filepath)), FullLoader))
        return data
