from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jsonn
from gendiff.diff_maker import make_diff
from gendiff.parser import parse, get_content_and_format


def generate_diff(filepath1, filepath2, format='stylish'):
    content1, format1 = get_content_and_format(filepath1)
    content2, format2 = get_content_and_format(filepath2)
    diff = make_diff(parse(content1, format1), parse(content2, format2))
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return jsonn(diff)
    else:
        return stylish(diff)
