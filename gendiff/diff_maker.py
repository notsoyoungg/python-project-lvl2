def make_diff(data1, data2):
    diff = []
    set_of_keys = sorted(list(set(list(data1.keys()) + list(data2.keys()))))
    for key in set_of_keys:
        if isinstance(data1.get(key), dict) and \
           isinstance(data2.get(key), dict):
            diff.append({
                'action': 'nested',
                'value': make_diff(data1[key], data2[key]),
                'key': key
            })
        elif data1.get(key) == data2.get(key):
            diff.append({
                'action': 'unchanged',
                'value': data1[key],
                'key': key
            })
        elif key not in data1:
            diff.append({
                'action': 'added',
                'value': data2[key],
                'key': key
            })
        elif key not in data2:
            diff.append({
                'action': 'removed',
                'value': data1[key],
                'key': key
            })
        else:
            diff.append({
                'action': 'changed',
                'old_value': data1[key],
                'new_value': data2[key],
                'key': key
            })
    return diff
