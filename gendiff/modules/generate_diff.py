from gendiff.modules.formatters.stylish import stylish


def generate_diff(diff, formatter=stylish):
    result = formatter(diff)
    return result
