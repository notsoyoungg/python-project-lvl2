def to_string(item, spaces):
    new_string = '{'
    chars = '    '
    for key, value in item.items():
        if isinstance(value, dict):
            new_string += f'\n{spaces}{key}: '
            new_string += to_string(value, spaces + chars)
        else:
            val = value.strip('"')
            new_string += f'\n{spaces}{key}: {val}'
    new_string += '\n' + spaces[len(chars):] + "}"
    return new_string


def format(item, spaces):
    if not isinstance(item, dict):
        return item.strip('"')
    else:
        return to_string(item, spaces)


KEYS_LIST = {'added': '+ ', 'removed': '- ', 'unchanged': '  '}


def stylish(diff, indent=''):
    chars = '    '
    string = '{'
    spaces = indent + chars
    for item in diff:
        if item['action'] == 'nested':
            string += f"\n{spaces[:-2]}  {item['key']}: "
            string += stylish(item['value'], spaces)
        if item['action'] == 'changed':
            string += f"\n{spaces[:-2]}- {item['key']}: "\
                      f"{format(item['old_value'], spaces + chars)}"
            string += f"\n{spaces[:-2]}+ {item['key']}: "\
                      f"{format(item['new_value'], spaces + chars)}"
        if item['action'] in KEYS_LIST:
            string += f"\n{spaces[:-2]}{KEYS_LIST[item['action']]}"\
                      f"{item['key']}: {format(item['value'], spaces + chars)}"
    string += '\n' + spaces[len(chars):] + "}"
    return string
