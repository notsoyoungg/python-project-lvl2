PROPERTY = "Property '"
ADDED = 'was added with value:'
REMOVED = 'was removed'
UPDATED = 'was updated. From'


def render_plain(diff):
    return iter_(diff)


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, int):
        return value
    return f"'{value}'"


def iter_(diff, parent=''):
    result = []
    for item in diff:
        full_path = f"{parent}.{item['key']}" if parent else f"{item['key']}"
        if item['action'] == 'added':
            result.append(f"{PROPERTY}{full_path}' {ADDED} "
                          f"{to_str(item['value'])}")
        if item['action'] == 'removed':
            result.append(f"{PROPERTY}{full_path}' {REMOVED}")
        if item['action'] == 'changed':
            result.append(f"{PROPERTY}{full_path}' {UPDATED} "
                          f"{to_str(item['old_value'])} to "
                          f"{to_str(item['new_value'])}")
        if item['action'] == 'nested':
            result.append(iter_(item['value'], full_path))
    return '\n'.join(result)
