from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonn


def format_diff(diff, format_name):
    if format_name == 'plain':
        return plain(diff)
    if format_name == 'json':
        return jsonn(diff)
    else:
        return stylish(diff)
