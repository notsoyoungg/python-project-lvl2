def make_diff(dict1, dict2):
    diff = []
    set_of_keys = sorted(list(set(list(dict1.keys()) + list(dict2.keys()))))
    for key in set_of_keys:
        if isinstance(dict1.get(key), dict) and \
           isinstance(dict2.get(key), dict):
            diff.append({
                'action': 'nested',
                'value': make_diff(dict1[key], dict2[key]),
                'key': key
            })
        elif dict1.get(key) == dict2.get(key):
            diff.append({
                'action': 'unchanged',
                'value': dict1[key],
                'key': key
            })
        elif key not in dict1:
            diff.append({
                'action': 'added',
                'value': dict2[key],
                'key': key
            })
        elif key not in dict2:
            diff.append({
                'action': 'removed',
                'value': dict1[key],
                'key': key
            })
        else:
            diff.append({
                'action': 'changed',
                'old_value': dict1[key],
                'new_value': dict2[key],
                'key': key
            })
    return diff
