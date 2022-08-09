from gendiff.formatters.formatter import format_diff
from gendiff.diff_maker import make_diff
from gendiff.parser import get_content


def generate_diff(filepath1, filepath2, format='stylish'):
    dict1 = get_content(filepath1)
    dict2 = get_content(filepath2)
    diff = make_diff(dict1, dict2)
    return format_diff(diff, format)
