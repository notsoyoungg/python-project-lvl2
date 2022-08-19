from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import make_json


def format_diff(diff, format_name):
    formatter_funcs = {
        'stylish': render_stylish,
        'plain': render_plain,
        'json': make_json
    }
    if format_name in formatter_funcs:
        return formatter_funcs[format_name](diff)
    raise Exception(f"Unrecognized formatter: {format_name}")
