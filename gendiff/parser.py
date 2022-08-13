import json
import yaml
from os.path import abspath


def parse(content, format):
    if format == 'json':
        data = json.load(content)
        return data
    if format in ('yaml', 'yml'):
        data = yaml.safe_load(content)
        return data
    raise Exception(f"Unrecognized format: {format}")


def get_content(filepath):
    content = open(abspath(filepath))
    extension = filepath.split('.')[-1]
    return parse(content, extension)
