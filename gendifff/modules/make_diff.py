def sort_dict(dict_):
    sorted_tuple = sorted(dict_.items(), key=lambda x: x[0])
    sorted_dict = dict(sorted_tuple)
    for key in sorted_dict:
        if isinstance(sorted_dict[key], bool):
            sorted_dict[key] = str(sorted_dict[key]).lower()
    return sorted_dict


def generate_diff(dict1, dict2):
    string = ['{ ']
    copy_for_job1 = sort_dict(dict1)
    copy_for_job2 = sort_dict(dict2)
    for key in copy_for_job1:
        if key in dict2 and dict1[key] == dict2[key]:
            string.append(f'    {key}: {copy_for_job1[key]}')
        if key not in dict2:
            string.append(f'  - {key}: {copy_for_job1[key]}')
        if key in dict2 and dict1[key] != dict2[key]:
            string.append(f'  - {key}: {copy_for_job1[key]}')
            string.append(f'  + {key}: {copy_for_job2[key]}')
    for key in copy_for_job2:
        if key not in dict1:
            string.append(f'  + {key}: {copy_for_job2[key]}')
    string.append('}')
    return '\n'.join(string)
