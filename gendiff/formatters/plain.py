def format_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return value.replace('"', "'")


def join_to_path(parent, child):
    if parent:
        return f"{parent}.{child}"
    else:
        return child


PROP = "Property '"
ADD = 'was added with value:'
RM = 'was removed'
UPD = 'was updated. From'


def plain(diff, parent=''):
    string = []
    for item in diff:
        full_path = join_to_path(parent, item['key'])
        if item['action'] == 'added':
            string.append(f"{PROP}{full_path}' {ADD} "
                          f"{format_val(item['value'])}")
        if item['action'] == 'removed':
            string.append(f"{PROP}{full_path}' {RM}")
        if item['action'] == 'changed':
            string.append(f"{PROP}{full_path}' {UPD} "
                          f"{format_val(item['old_value'])} to "
                          f"{format_val(item['new_value'])}")
        if item['action'] == 'nested':
            string.append(plain(item['value'], full_path))
    return '\n'.join(string)
