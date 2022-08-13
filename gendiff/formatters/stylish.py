import json


EXCEPTION_VALUES = [True, False, None]
VALUE_STATUSES = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def format_value(item):
    if item in EXCEPTION_VALUES:
        return json.dumps(item)
    else:
        return item


def make_string(item, spaces):
    result = '{'
    tabs = '    '
    for key, value in item.items():
        if isinstance(value, dict):
            result += f'\n{spaces}{key}: '
            result += make_string(value, spaces + tabs)
        else:
            result += f'\n{spaces}{key}: {format_value(value)}'
    result += '\n' + spaces[len(tabs):] + "}"
    return result


def format(item, spaces):
    if not isinstance(item, dict):
        return format_value(item)
    else:
        return make_string(item, spaces)


def make_stylish(diff, indent=''):
    tabs = '    '
    result = '{'
    spaces = indent + tabs
    for item in diff:
        if item['action'] == 'nested':
            result += f"\n{spaces[:-2]}  {item['key']}: "
            result += make_stylish(item['value'], spaces)
        if item['action'] == 'changed':
            result += f"\n{spaces[:-2]}- {item['key']}: "\
                      f"{format(item['old_value'], spaces + tabs)}"
            result += f"\n{spaces[:-2]}+ {item['key']}: "\
                      f"{format(item['new_value'], spaces + tabs)}"
        if item['action'] in VALUE_STATUSES:
            result += f"\n{spaces[:-2]}{VALUE_STATUSES [item['action']]}"\
                      f"{item['key']}: {format(item['value'], spaces + tabs)}"
    result += '\n' + spaces[len(tabs):] + "}"
    return result
