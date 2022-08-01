from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonn
from gendiff.diff_maker import make_diff
from gendiff.parser import get_data, get_format


def generate_diff(filepath1, filepath2, format='stylish'):
    diff = make_diff(get_data(filepath1, get_format(filepath1)),
                     get_data(filepath2, get_format(filepath2)))
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return jsonn(diff)
    else:
        return stylish(diff)
