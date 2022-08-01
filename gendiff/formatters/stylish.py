from gendiff.diff_maker import KEYS_LIST


def stylish(diff_dictionaary):  # noqa: C901
    chars = '    '

    def walk(dictionary, chars):
        chars2 = '    '
        string = '{'
        for key, value in dictionary.items():
            if not isinstance(value, dict) and not isinstance(value, list):
                val = value.strip('"')
            if not isinstance(value, dict):
                if key[0:2] == '+ ' or key[0:2] == '- ':
                    string += f"\n{chars[:-2]}{key}: {val}"
                if key[0:2] == '-+':
                    first = value[0]
                    second = value[1]
                    if isinstance(first, dict):
                        val = second.strip('"')
                        string += f'\n{chars[:-2]}- {key[3:]}: '
                        string += walk(first, chars + chars2)
                        string += f"\n{chars[:-2]}+ {key[3:]}: {val}"
                    if isinstance(second, dict):
                        val = first.strip('"')
                        string += f"\n{chars[:-2]}- {key[3:]}: {val}"
                        string += f'\n{chars[:-2]}+ {key[3:]}: '
                        string += walk(second, chars + chars2)
                    if not isinstance(first, dict) and \
                       not isinstance(second, dict):
                        val1 = first.strip('"')
                        val2 = second.strip('"')
                        string += f"\n{chars[:-2]}- {key[3:]}: {val1}"
                        string += f"\n{chars[:-2]}+ {key[3:]}: {val2}"
                if key[0:2] not in KEYS_LIST:
                    val = value.strip('"')
                    string += f"\n{chars}{key}: {val}"
            if isinstance(value, dict):
                if key[0:2] in KEYS_LIST:
                    string += f'\n{chars[:-2]}{key[0]} {key[2:]}: '
                    string += walk(value, chars + chars2)
                else:
                    string += f'\n{chars}{key}: '
                    string += walk(value, chars + chars2)
        string += '\n' + chars[len(chars2):] + "}"
        return string
    return walk(diff_dictionaary, chars)
