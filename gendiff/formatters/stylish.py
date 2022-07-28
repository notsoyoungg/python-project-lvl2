import ast


def make_string(string, spaces):
    to_dict = ast.literal_eval(string)

    def walk(dictionary, spaces):
        new_string = '{'
        chars = '    '
        for key, value in dictionary.items():
            if isinstance(value, dict):
                new_string += f'\n{spaces}{key}: '
                new_string += walk(value, spaces + chars)
            else:
                new_string += f'\n{spaces}{key}: {value}'
        new_string += '\n' + spaces[len(chars):] + "}"
        return new_string
    return walk(to_dict, spaces)


def stylish(diff_dictionaary):
    chars = '    '

    def walk(dictionary, chars):
        chars2 = '    '
        string = '{'
        for key, value in dictionary.items():
            if not isinstance(value, dict):
                if key[0] == '=':
                    string += f'\n{chars[:-2]}  {value}'
                if key[0:2] == '+ ':
                    string += f'\n{chars[:-2]}+ {value}'
                if key[0:2] == '- ':
                    string += f'\n{chars[:-2]}- {value}'
                if key[0:2] == '-+':
                    first = value.split(' * ')[0]
                    second = value.split(' * ')[1]
                    first_plus_char = first + ' '
                    second_plus_char = second + ' '
                    if first_plus_char[0] == '{':
                        string += f'\n{chars[:-2]}- {key[3:]}: '
                        string += make_string(first, chars + chars2)
                        string += f'\n{chars[:-2]}+ {key[3:]}: {second}'
                    if second_plus_char == '{':
                        string += f'\n{chars[:-2]}- {key[3:]}: {first}'
                        string += f'\n{chars[:-2]}+ {key[3:]}: '
                        string += make_string(second, chars + chars2)
                    if first_plus_char[0] != '{' and second_plus_char != '{':
                        string += f'\n{chars[:-2]}- {key[3:]}: {first}'
                        string += f'\n{chars[:-2]}+ {key[3:]}: {second}'
                if key[0] != '=' and key[0:2] != '+ ' and key[0:2] != '- ' and key[0:2] != '+-' and key[0:2] != '-+':
                    string += f'\n{chars}{value}'
            if isinstance(value, dict):
                if key[0:2] == '+ ':
                    string += f'\n{chars[:-2]}+ {key[2:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] == '- ':
                    string += f'\n{chars[:-2]}- {key[2:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] == '-+':
                    string += f'\n{chars[:-2]}- {key[3:]}: '
                    string += walk(value, chars + chars2)
                if key[0:2] != '+ ' and key[0:2] != '- ' and key and key[0:2] != '-+':
                    string += f'\n{chars}{key}: '
                    string += walk(value, chars + chars2)
        string += '\n' + chars[len(chars2):] + "}"
        return string
    return walk(diff_dictionaary, chars)
