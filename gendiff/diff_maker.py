KEYS_LIST = ['+ ', '- ', '-+']


def make_diff(dict1, dict2):
    diff_dict = {}
    set_of_keys = sorted(list(set(list(dict1.keys()) + list(dict2.keys()))))
    for key in set_of_keys:
        if isinstance(dict1.get(key), dict) and \
           isinstance(dict2.get(key), dict):
            diff_dict[key] = make_diff(dict1[key], dict2[key])
        elif dict1.get(key) == dict2.get(key):
            diff_dict[key] = dict1[key]
        elif key not in dict1:
            diff_dict[f'+ {key}'] = dict2[key]
        elif key not in dict2:
            diff_dict[f'- {key}'] = dict1[key]
        else:
            diff_dict[f'-+ {key}'] = [dict1[key], dict2[key]]
    return diff_dict
