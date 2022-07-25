import json
import os.path
import yaml
from yaml.loader import FullLoader


def sort_dict(dict_):
    sorted_tuple = sorted(dict_.items(), key=lambda x: x[0])
    sorted_dict = dict(sorted_tuple)
    for key in sorted_dict:
        if isinstance(sorted_dict[key], dict):
            sorted_dict[key] = sort_dict(sorted_dict[key])
    return sorted_dict


def format_dict(dict_):
    for key in dict_:
        if isinstance(dict_[key], bool):
            dict_[key] = str(dict_[key]).lower()
        if dict_[key] is None:
            dict_[key] = 'null'
        if isinstance(dict_[key], int):
            dict_[key] = str(dict_[key])
        if isinstance(dict_[key], dict):
            format_dict(dict_[key])        
    return dict_


path = 'base/some2.json'
yml_readed = yaml.load(open('base/file1.yml'), FullLoader)
yml_readed2 = yaml.load(open('base/file2.yaml'), FullLoader)
readed = json.load(open('base/some.json'))
readed2 = json.load(open('base/some2.json'))
for_diff1 = format_dict(sort_dict(readed))
for_diff2 = format_dict(sort_dict(readed2))
yaml1 = format_dict(sort_dict(yml_readed))
yaml2 = format_dict(sort_dict(yml_readed2))
set_of_keys = set(list(for_diff1.keys()) + list(for_diff2.keys()))
#print(sorted(list(set_of_keys)))
#print(yml_readed)
#print(path[-4:])


dictionary = {'hello': 'Garry', 'box': 20, 'dict': {"some": 2}}
#print(stringify(dictionary, replacer='#', count=1))
string = str(dictionary)
#print(string)


def stringify(value, replacer=' ', count=1):
    if isinstance(value, dict):
        chars = replacer * count
        def walk(dictionary, chars):
            chars2 = replacer * count
            string = '{'
            for key in dictionary:
                if not isinstance(dictionary[key], dict):
                    string += f'\n{chars}{key}: {dictionary[key]}'
                if isinstance(dictionary[key], dict):
                    string += f'\n{chars}{key}: '
                    string += walk(dictionary[key], chars + chars2)
            string += '\n' + chars[len(chars2):] + "}"
            return string
    else:
        return str(value)
    return walk(value, chars)


#print(stringify(primitives, ' '))
#print(stringify(data))
def make_dict_in_diff(dictionary):
    diff_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            diff_dict[f'{key}'] = make_dict_in_diff(value)
        else:
            diff_dict[f'{key}'] = f'{key}: {value}'
    return diff_dict


def generate_diff2(dict1, dict2):
    diff_dict = {}
    set_of_keys = sorted(list(set(list(dict1.keys()) + list(dict2.keys()))))
    for key in set_of_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                if isinstance(dict1[key], dict):
                    diff_dict[key] = generate_diff2(dict1[key], dict2[key])
                else:
                    diff_dict[f'= {key}'] = f'{key}: {dict1[key]}'
            if dict1[key] != dict2[key]:
                if isinstance(dict1[key], dict) == isinstance(dict2[key], dict) == True:
                    diff_dict[key] = generate_diff2(dict1[key], dict2[key])
                if isinstance(dict1[key], dict) and  isinstance(dict2[key], dict) == False:
                    diff_dict[f'-+ {key}'] = make_dict_in_diff(dict1[key])
                    diff_dict[f'+- {key}'] = f'{key}: {dict2[key]}'
                if isinstance(dict2[key], dict) and  isinstance(dict1[key], dict) == False:
                    diff_dict[f'-+ {key}'] = f'{key}: {dict1[key]}'
                    diff_dict[f'+- {key}'] = make_dict_in_diff(dict2[key])
                if isinstance(dict1[key], dict) == isinstance(dict2[key], dict) == False:
                    diff_dict[f'-+ {key}'] = f'{key}: {dict1[key]}'
                    diff_dict[f'+- {key}'] = f'{key}: {dict2[key]}'
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


#print(generate_diff2(readed, readed2))
diff = generate_diff2(yaml1, yaml2)
diff2 = generate_diff2(for_diff1, for_diff2)
print(diff)
print(diff2)

def stylish2(diff_dictionaary):
    chars = '////'
    def walk(dictionary, chars):
        chars2 = '////'
        string = '{ '
        for key, value in dictionary.items():
            if not isinstance(value, dict):
                if key[0] == '=':
                    string += f'\n{chars[:-2]}  {value}'
                if key[0:2] == '+ ':
                    string += f'\n{chars[:-2]}+ {value}'
                if key[0:2] == '- ':
                    string += f'\n{chars[:-2]}- {value}'
                if key[0:2] == '-+':
                    string += f'\n{chars[:-2]}- {value}'
                if key[0:2] == '+-':
                    string += f'\n{chars[:-2]}+ {value}'
                if key[0] != '=' and key[0:2] != '+ ' and key[0:2] != '- ' and key[0:2] != '+-' and key[0:2] != '-+':
                    string += f'\n{chars}{value}'
            if isinstance(value, dict):
                if key[0:2] == '+ ':
                    string += f'\n{chars[:-2]}+ {key[2:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] == '- ':
                    string += f'\n{chars[:-2]}- {key[2:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] == '+-':
                    string += f'\n{chars[:-2]}+ {key[3:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] == '-+':
                    string += f'\n{chars[:-2]}- {key[3:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] != '+ ' and key[0:2] != '- ' and key[0:2] != '+-' and key[0:2] != '-+':
                    string += f'\n{chars}{key}: '
                    string += walk(value, chars + chars2)
        string += '\n' + chars[len(chars2):] + "}"
        return string
    return walk(diff_dictionaary, chars)

print(stylish2(diff))
print(stylish2(diff2))

def stylish3(diff_dictionary):
    prop = "Property '"
    add = 'was added with value:'
    rm = 'was remowed'
    upd = 'was updated. From'
    val = '[complex value]'
    def walk(dictionary, chars, depth):
        chars2 = "Property '"
        string = ''
        for key, value in dictionary.items():
            if not isinstance(value, dict):
                if key[0:2] == '+ ':
                    string += f"{chars}{key[2:]}' {add}{value[len(key) - 1:]}\n"
                if key[0:2] == '- ':
                    string += f"{chars}{key[2:]}' {rm}\n"
                if key[0:2] == '-+':
                    string += f"{chars}{key[3:]}' {upd} {value[len(key) - 1:]} to "
                if key[0:2] == '+-':
                    string += f"{value[len(key) - 1:]}\n"
            if isinstance(value, dict):
                print('dict')
                print(key)
                if key[0:2] == '+ ':
                    string += f"{chars2}{key[2:]}' {add} {val}\n"
                if key[0:2] == '- ':
                    string += f"{chars2}{key[2:]}' {rm}\n"
                if key[0:2] == '-+':
                    print('jepa')
                    string += f"{chars2}{key[3:]}."
                    string += walk(value, ' ', depth + 1)
                if key[0:2] == '+-':
                    print('abracadabra')
                    string += f"{chars2}{key[3:]}."
                    string += 'плюс минус\n'
                if key[0:2] != '+ ' and key[0:2] != '- ' and key[0:2] != '+-' and key[0:2] != '-+':
                    print('babayaga')
                    string += f"{chars2}{key}."
                    string += 'вот она рыба\n'
                    string += walk(value, ' ', depth + 1)
                    
        return string
    return walk(diff_dictionary, prop, 0)
            


print(stylish3(diff))
print(stylish3(diff2))