from os.path import abspath
from gendiff.gendiff import generate_diff


def test_diff_plain():
    dict1_json = './tests/fixtures/plain_file1.json'
    dict2_json = './tests/fixtures/plain_file2.json'
    dict1_yml = './tests/fixtures/plain_filepath.yml'
    dict2_yml = './tests/fixtures/plain_filepath2.yaml'
    result = open(abspath(
        './tests/fixtures/result_plain.txt'
    ), 'r').read()
    assert generate_diff(dict1_json, dict2_json) == result
    assert generate_diff(dict1_yml, dict2_yml) == result
    assert generate_diff(dict1_yml, dict2_json) == result


def test_diff_recursive_stylish():
    dict1_json = './tests/fixtures/file1.json'
    dict2_json = './tests/fixtures/file2.json'
    dict1_yml = './tests/fixtures/file_yml1.yml'
    dict2_yml = './tests/fixtures/file_yml2.yml'
    result = open(abspath(
        './tests/fixtures/result_recursive.txt'
    ), 'r').read()
    assert generate_diff(dict1_json, dict2_json) == result
    assert generate_diff(dict1_yml, dict2_yml) == result
    assert generate_diff(dict1_yml, dict2_json) == result


def test_diff_recursive_plain():
    dict1_json = './tests/fixtures/file1.json'
    dict2_json = './tests/fixtures/file2.json'
    dict1_yml = './tests/fixtures/file_yml1.yml'
    dict2_yml = './tests/fixtures/file_yml2.yml'
    result = open(abspath(
        './tests/fixtures/result_recursive_plain.txt'
    ), 'r').read()
    assert generate_diff(dict1_json, dict2_json, 'plain') == result
    assert generate_diff(dict1_yml, dict2_yml, 'plain') == result
    assert generate_diff(dict1_yml, dict2_json, 'plain') == result


def test_diff_recursive_json():
    dict1_json = './tests/fixtures/file1.json'
    dict2_json = './tests/fixtures/file2.json'
    dict1_yml = './tests/fixtures/file_yml1.yml'
    dict2_yml = './tests/fixtures/file_yml2.yml'
    result = open(abspath(
        './tests/fixtures/result_json.txt'
    ), 'r').read()
    assert generate_diff(dict1_json, dict2_json, 'json') == result
    assert generate_diff(dict1_yml, dict2_yml, 'json') == result
    assert generate_diff(dict1_yml, dict2_json, 'json') == result
