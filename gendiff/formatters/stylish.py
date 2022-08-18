import json


NON_FORMAT_VALUES = [True, False, None]
ACTION_PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def to_str(item, spaces):
    if isinstance(item, dict):
        result = '{'
        tabs = '    '
        for key, value in item.items():
            if isinstance(value, dict):
                result += f'\n{spaces}{key}: '
                result += to_str(value, spaces + tabs)
            else:
                if value in NON_FORMAT_VALUES:
                    result += f'\n{spaces}{key}: {json.dumps(value)}'
                else:
                    result += f'\n{spaces}{key}: {value}'
        result += '\n' + spaces[len(tabs):] + "}"
        return result
    else:
        if item in NON_FORMAT_VALUES:
            return json.dumps(item)
        else:
            return item


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
                      f"{to_str(item['old_value'], spaces + tabs)}"
            result += f"\n{spaces[:-2]}+ {item['key']}: "\
                      f"{to_str(item['new_value'], spaces + tabs)}"
        if item['action'] in ACTION_PREFIXES:
            result += f"\n{spaces[:-2]}{ACTION_PREFIXES [item['action']]}"\
                      f"{item['key']}: {to_str(item['value'], spaces + tabs)}"
    result += '\n' + spaces[len(tabs):] + "}"
    return result
