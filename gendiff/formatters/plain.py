import json


EXCEPTION_VALUES = [True, False, None]
PROP = "Property '"
ADD = 'was added with value:'
RM = 'was removed'
UPD = 'was updated. From'


def format_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        if value in EXCEPTION_VALUES:
            return json.dumps(value)
        else:
            return f"'{value}'"


def join_to_path(parent, child):
    if parent:
        return f"{parent}.{child}"
    else:
        return child


def make_plain(diff, parent=''):
    result = []
    for item in diff:
        full_path = join_to_path(parent, item['key'])
        if item['action'] == 'added':
            result.append(f"{PROP}{full_path}' {ADD} "
                          f"{format_val(item['value'])}")
        if item['action'] == 'removed':
            result.append(f"{PROP}{full_path}' {RM}")
        if item['action'] == 'changed':
            result.append(f"{PROP}{full_path}' {UPD} "
                          f"{format_val(item['old_value'])} to "
                          f"{format_val(item['new_value'])}")
        if item['action'] == 'nested':
            result.append(make_plain(item['value'], full_path))
    return '\n'.join(result)
