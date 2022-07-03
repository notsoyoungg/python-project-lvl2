def sort_dict(dict_):
    sorted_tuple = sorted(dict_.items(), key=lambda x: x[0])
    sorted_dict = dict(sorted_tuple)
    return sorted_dict


def generate_diff(dict1, dict2):
    string = []
    for key in sort_dict(dict1):
        if key in dict2 and dict1[key] == dict2[key]:
            string.append(f'  {key}: {dict1[key]}')
        if key not in dict2:
            string.append(f'- {key}: {dict1[key]}')
        if key in dict2 and dict1[key] != dict2[key]:
            string.append(f'- {key}: {dict1[key]}')
            string.append(f'+ {key}: {dict2[key]}')
    for key in sort_dict(dict2):
        if key not in dict1:
            string.append(f'+ {key}: {dict2[key]}')
    return '\n'.join(string)
