import json


EXCEPTION_VALUES = [True, False, None]
PROPERTY = "Property '"
ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'


def format_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        if value in EXCEPTION_VALUES:
            return json.dumps(value)
        else:
            return f"'{value}'"


def make_plain(diff, parent=''):
    result = []
    for item in diff:
        full_path = f"{parent}.{item['key']}" if parent else f"{item['key']}"
        if item['action'] == 'added':
            result.append(f"{PROPERTY}{full_path}' {ADDED} "
                          f"{format_val(item['value'])}")
        if item['action'] == 'removed':
            result.append(f"{PROPERTY}{full_path}' {REMOVED}")
        if item['action'] == 'changed':
            result.append(f"{PROPERTY}{full_path}' {UPDATED} "
                          f"{format_val(item['old_value'])} to "
                          f"{format_val(item['new_value'])}")
        if item['action'] == 'nested':
            result.append(make_plain(item['value'], full_path))
    return '\n'.join(result)
