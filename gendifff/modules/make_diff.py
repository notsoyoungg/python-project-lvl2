def make_dict_in_diff(dictionary):
    diff_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            diff_dict[f'{key}'] = make_dict_in_diff(value)
        else:
            diff_dict[f'{key}'] = f'{key}: {value}'
    return diff_dict


def make_diff(dict1, dict2):
    diff_dict = {}
    set_of_keys = sorted(list(set(list(dict1.keys()) + list(dict2.keys()))))
    for key in set_of_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                if isinstance(dict1[key], dict):
                    diff_dict[key] = make_diff(dict1[key], dict2[key])
                else:
                    diff_dict[f'= {key}'] = f'{key}: {dict1[key]}'
            if dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) == isinstance(dict2[key], dict) == True:
                    diff_dict[key] = make_diff(dict1[key], dict2[key])
                else:
                    diff_dict[f'-+ {key}'] = f'{dict1[key]} * {dict2[key]}'
        if key not in dict1:
            if not isinstance(dict2[key], dict):
                diff_dict[f'+ {key}'] = f'{key}: {dict2[key]}'
            else:
                diff_dict[f'+ {key}'] = make_dict_in_diff(dict2[key])
        if key not in dict2:
            if not isinstance(dict1[key], dict):
                diff_dict[f'- {key}'] = f'{key}: {dict1[key]}'
            else:
                diff_dict[f'- {key}'] = make_dict_in_diff(dict1[key])
    return diff_dict
