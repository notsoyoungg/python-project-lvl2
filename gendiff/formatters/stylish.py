from gendiff.diff_maker import KEYS_LIST


def to_string(item, spaces):
    new_string = '{'
    chars = '    '
    for key, value in item.items():
        if isinstance(value, dict):
            new_string += f'\n{spaces}{key}: '
            new_string += to_string(value, spaces + chars)
        else:
            val = value.strip('"')
            new_string += f'\n{spaces}{key}: {val}'
    new_string += '\n' + spaces[len(chars):] + "}"
    return new_string


def format(item, spaces):
    if not isinstance(item, dict):
        return item.strip('"')
    else:
        return to_string(item, spaces)


def stylish(diff_dictionaary):  # noqa: C901
    chars = '    '

    def walk(dictionary, chars):
        chars2 = '    '
        string = '{'
        for key, value in dictionary.items():
            if isinstance(value, dict):
                if key[0:2] in KEYS_LIST:
                    string += f'\n{chars[:-2]}{key[0]} {key[2:]}: '
                    string += walk(value, chars + chars2)
                else:
                    string += f'\n{chars}{key}: '
                    string += walk(value, chars + chars2)
            elif key[0:2] == '+ ' or key[0:2] == '- ':
                string += f"\n{chars[:-2]}{key}: {format(value, chars + chars2)}"
            elif key[0:2] == '-+':
                first = value[0]
                second = value[1]
                string += f"\n{chars[:-2]}- {key[3:]}: "\
                          f"{format(first, chars + chars2)}"
                string += f"\n{chars[:-2]}+ {key[3:]}: "\
                          f"{format(second, chars + chars2)}"
            elif key[0:2] not in KEYS_LIST:
                string += f"\n{chars}{key}: {format(value, chars + chars2)}"
        string += '\n' + chars[len(chars2):] + "}"
        return string
    return walk(diff_dictionaary, chars)
