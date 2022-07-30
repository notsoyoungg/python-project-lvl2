def plain(diff_dictionary):  # noqa: C901
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
                    new_val = value.replace('"', "'")
                    string += f"\n{chars}{key[2:]}' {add} {new_val}"
            if key[0:2] == '- ':
                string += f"\n{chars}{key[2:]}' {rm}"
            if key[0:2] == '-+':
                first = value[0]
                second = value[1]
                if isinstance(first, dict):
                    new_val = second.replace('"', "'")
                    string += f"\n{chars}{key[3:]}' {upd} {val} to {new_val}"
                if isinstance(second, dict):
                    new_val = first.replace('"', "'")
                    string += f"\n{chars}{key[3:]}' {upd} {new_val} to {val}"
                if not isinstance(first, dict) and not isinstance(second, dict):
                    val1 = first.replace('"', "'")
                    val2 = second.replace('"', "'")
                    string += f"\n{chars}{key[3:]}' {upd} {val1} to {val2}"
            if key[0:2] != '+ ' and key[0:2] != \
               '- ' and key[0:2] != '-+' and key[0:2] != '= ':
                string += walk(value, chars + f'{key}.')
        return string
    return walk(diff_dictionary, prop).strip()
