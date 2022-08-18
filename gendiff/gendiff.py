import gendiff.formatters
from gendiff.dicts_diff import make_diff
from gendiff.parser import get_content


def generate_diff(filepath1, filepath2, format='stylish'):
    content1 = get_content(filepath1)
    content2 = get_content(filepath2)
    diff = make_diff(content1, content2)
    return gendiff.formatters.format_diff(diff, format)
