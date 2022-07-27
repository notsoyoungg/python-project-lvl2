def is_exception(string):
    list_of_values = ['true', 'false', 'null']
    for value in list_of_values:
        if value == string:
            return True
    return False


def plain(diff_dictionary):
    prop = "Property '"
    add = 'was added with value:'
    rm = 'was removed'
    upd = 'was updated. From'
    val = '[complex value]'

    def walk(dictionary, chars):
        string = ''
        chars2 = "Property '"
        chars2 += chars
        for key, value in dictionary.items():
            if key[0:2] == '+ ':
                if isinstance(value, dict):
                    string += f"\n{chars}{key[2:]}' {add} {val}"
                else:
                    if is_exception(value[len(key):]):
                        string += f"\n{chars}{key[2:]}' {add} {value[len(key):]}"
                    else:
                        string += f"\n{chars}{key[2:]}' {add} '{value[len(key):]}'"
            if key[0:2] == '- ':
                string += f"\n{chars}{key[2:]}' {rm}"
            if key[0:2] == '-+':
                first = value.split(' * ')[0]
                second = value.split(' * ')[1]
                first_plus_char = first + ' '
                second_plus_char = second + ' '
                if first_plus_char[0] == '{':
                    if is_exception(second):
                        string += f"\n{chars}{key[3:]}' {upd} {val} to {second}"
                    else:
                        string += f"\n{chars}{key[3:]}' {upd} {val} to '{second}'"
                if second_plus_char[0] == '{':
                    if is_exception(first):
                        string += f"\n{chars}{key[3:]}' {upd} {first} to {val}"
                    else:
                        string += f"\n{chars}{key[3:]}' {upd} '{first}' to {val}"
                if first_plus_char[0] != '{' and second_plus_char[0] != '{':
                    if is_exception(first) and not is_exception(second):
                        string += f"\n{chars}{key[3:]}' {upd} {first} to '{second}'"
                    if is_exception(second) and not is_exception(first):
                        string += f"\n{chars}{key[3:]}' {upd} '{first}' to {second}"
                    if is_exception(first) and is_exception(second):
                        string += f"\n{chars}{key[3:]}' {upd} {first} to {second}"
                    else:
                        string += f"\n{chars}{key[3:]}' {upd} '{first}' to '{second}'"
            if key[0:2] != '+ ' and key[0:2] != '- ' and key[0:2] != '-+' and key[0:2] != '= ':
                string += walk(value, chars + f'{key}.')
        return string
    return walk(diff_dictionary, prop).strip()