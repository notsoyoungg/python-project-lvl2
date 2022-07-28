from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonn
from gendiff.make_diff import make_diff
from gendiff.parser import parse


def generate_diff(file1, file2, format='stylish'):
    diff = make_diff(parse(file1), parse(file2))
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return jsonn(diff)
    else:
        return stylish(diff)
