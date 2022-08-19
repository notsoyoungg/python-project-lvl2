ACTION_PREFIXES = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def render_stylish(diff):
    return iter_(diff)


def format_bool_and_nonetype(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def to_str(item, spaces):
    if isinstance(item, dict):
        result = '{'
        tabs = '    '
        for key, value in item.items():
            if isinstance(value, dict):
                result += f'\n{spaces}{key}: '
                result += to_str(value, spaces + tabs)
            else:
                result += f'\n{spaces}{key}: {format_bool_and_nonetype(value)}'
        result += '\n' + spaces[len(tabs):] + "}"
        return result
    return format_bool_and_nonetype(item)


def iter_(diff, indent=''):
    tabs = '    '
    result = '{'
    spaces = indent + tabs
    for item in diff:
        if item['action'] == 'nested':
            result += f"\n{spaces[:-2]}  {item['key']}: "
            result += iter_(item['value'], spaces)
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
