import argparse
import json
from os.path import abspath
import yaml
from yaml.loader import FullLoader
from gendiff.modules.formatters.stylish import stylish
from gendiff.modules.formatters.plain import plain
from gendiff.modules.formatters.json import jsonn


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default=stylish,
                    help='output format (default: "stylish")')
args = parser.parse_args()


def sort_dict(dict_):
    sorted_tuple = sorted(dict_.items(), key=lambda x: x[0])
    sorted_dict = dict(sorted_tuple)
    for key in sorted_dict:
        if isinstance(sorted_dict[key], dict):
            sorted_dict[key] = sort_dict(sorted_dict[key])
    return sorted_dict


def format_dict(dict_):
    for key in dict_:
        if isinstance(dict_[key], bool):
            dict_[key] = json.dumps(dict_[key])
        if dict_[key] is None:
            dict_[key] = json.dumps(dict_[key])
        if isinstance(dict_[key], int):
            dict_[key] = str(dict_[key])
        if isinstance(dict_[key], dict):
            format_dict(dict_[key])
    return dict_


if args.first_file[-4:] == 'json':
    readed = format_dict(sort_dict(json.load(open(abspath(args.first_file)))))
else:
    readed = format_dict(sort_dict(yaml.load(open(abspath(args.first_file)), FullLoader)))
if args.second_file[-4:] == 'json':
    readed2 = format_dict(sort_dict(json.load(open(abspath(args.second_file)))))
else:
    readed2 = format_dict(sort_dict(yaml.load(open(abspath(args.second_file)), FullLoader)))
if args.format == 'plain':
    args.format = plain
if args.format == 'json':
    args.format = jsonn
