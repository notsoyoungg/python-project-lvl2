import json
from yaml import load
from yaml.loader import FullLoader
from os.path import abspath
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.formatters.plain import plain
from gendiff.modules.formatters.json import jsonn
from gendiff.modules.make_diff import make_diff


# хотел импортировать две функции ниже из модуля 'pars',
# но в таком случае тесты падают с ошибкой как-то связанной с парсером
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
            dict_[key] = json.dumps(dict_[key])
        if dict_[key] is None:
            dict_[key] = json.dumps(dict_[key])
        if isinstance(dict_[key], int):
            dict_[key] = str(dict_[key])
        if isinstance(dict_[key], dict):
            format_dict(dict_[key])
    return dict_


def test_diff_plain():
    dict1_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/plain_file1.json'
    )))))
    dict2_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/plain_file2.json'
    )))))
    dict1_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/plain_filepath.yml'
    )), FullLoader)))
    dict2_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/plain_filepath2.yaml'
    )), FullLoader)))
    result = open(abspath(
        './gendiff/tests/fixtures/result_plain.txt'
    ), 'r').read()
    assert generate_diff(make_diff(dict1_json, dict2_json)) == result
    assert generate_diff(make_diff(dict1_yml, dict2_yml)) == result
    assert generate_diff(make_diff(dict1_yml, dict2_json)) == result


def test_diff_recursive_stylish():
    dict1_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file1.json'
    )))))
    dict2_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file2.json'
    )))))
    dict1_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml1.yml'
    )), FullLoader)))
    dict2_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml2.yml'
    )), FullLoader)))
    result = open(abspath(
        './gendiff/tests/fixtures/result_recursive.txt'
    ), 'r').read()
    assert generate_diff(make_diff(dict1_json, dict2_json)) == result
    assert generate_diff(make_diff(dict1_yml, dict2_yml)) == result
    assert generate_diff(make_diff(dict1_yml, dict2_json)) == result


def test_diff_recursive_plain():
    dict1_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file1.json'
    )))))
    dict2_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file2.json'
    )))))
    dict1_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml1.yml'
    )), FullLoader)))
    dict2_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml2.yml'
    )), FullLoader)))
    result = open(abspath(
        './gendiff/tests/fixtures/result_recursive_plain.txt'
    ), 'r').read()
    assert generate_diff(make_diff(dict1_json, dict2_json), plain) == result
    assert generate_diff(make_diff(dict1_yml, dict2_yml), plain) == result
    assert generate_diff(make_diff(dict1_yml, dict2_json), plain) == result


def test_diff_recursive_json():
    dict1_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file1.json'
    )))))
    dict2_json = format_dict(sort_dict(json.load(open(abspath(
        './gendiff/tests/fixtures/file2.json'
    )))))
    dict1_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml1.yml'
    )), FullLoader)))
    dict2_yml = format_dict(sort_dict(load(open(abspath(
        './gendiff/tests/fixtures/file_yml2.yml'
    )), FullLoader)))
    result = open(abspath(
        './gendiff/tests/fixtures/result_json.txt'
    ), 'r').read()
    assert generate_diff(make_diff(dict1_json, dict2_json), jsonn) == result
    assert generate_diff(make_diff(dict1_yml, dict2_yml), jsonn) == result
    assert generate_diff(make_diff(dict1_yml, dict2_json), jsonn) == result
