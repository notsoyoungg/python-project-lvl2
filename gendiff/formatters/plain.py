from gendiff.diff_maker import KEYS_LIST


def format_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return value.replace('"', "'")


PROP = "Property '"
ADD = 'was added with value:'
RM = 'was removed'
UPD = 'was updated. From'


def plain(diff_dictionary):  # noqa: C901

    def walk(dictionary, chars):
        string = ''
        chars2 = "Property '"
        chars2 += chars
        for key, value in dictionary.items():
            if key[0:2] == '+ ':
                string += f"\n{chars}{key[2:]}' "\
                          f"{ADD} {format_val(value)}"
            elif key[0:2] == '- ':
                string += f"\n{chars}{key[2:]}' {RM}"
            elif key[0:2] == '-+':
                first = value[0]
                second = value[1]
                string += f"\n{chars}{key[3:]}' {UPD} "\
                          f"{format_val(first)} to {format_val(second)}"
            elif key[0:2] not in KEYS_LIST and isinstance(value, dict):
                string += walk(value, chars + f'{key}.')
        return string
    return walk(diff_dictionary, PROP).strip()
