from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonn


def generate_diff(diff, format='stylish'):
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return jsonn(diff)
    else:
        return stylish(diff)
