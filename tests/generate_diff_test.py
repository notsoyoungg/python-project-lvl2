import pytest
from os.path import abspath
from gendiff.gendiff import generate_diff


FIXTURE_PATH = './tests/fixtures/'


def build_filepath(file_name):
    if file_name[0:6] == 'result':
        return open(abspath(FIXTURE_PATH + file_name)).read()
    else:
        return FIXTURE_PATH + file_name


JSON_FLAT1 = build_filepath('plain_file1.json')
JSON_FLAT2 = build_filepath('plain_file2.json')
JSON_NESTED1 = build_filepath('file1.json')
JSON_NESTED2 = build_filepath('file2.json')
YML_FLAT1 = build_filepath('plain_filepath.yml')
YML_FLAT2 = build_filepath('plain_filepath2.yaml')
YML_NESTED1 = build_filepath('file_yml1.yml')
YML_NESTED2 = build_filepath('file_yml2.yml')
EXPECTED_FLAT = build_filepath('result_plain.txt')
EXPECTED_STYLISH = build_filepath('result_recursive.txt')
EXPECTED_PLAIN = build_filepath('result_recursive_plain.txt')
EXPECTED_JSON = build_filepath('result_json.txt')


@pytest.mark.parametrize("test_input1,test_input2,expected", [
                        (JSON_FLAT1, JSON_FLAT2, EXPECTED_FLAT),
                        (YML_FLAT1, YML_FLAT2, EXPECTED_FLAT),
                        (YML_FLAT1, JSON_FLAT2, EXPECTED_FLAT)])
def test_diff_plain(test_input1, test_input2, expected):
    assert generate_diff(test_input1, test_input2) == expected


@pytest.mark.parametrize("test_input1,test_input2,expected", [
                        (JSON_NESTED1, JSON_NESTED2, EXPECTED_STYLISH),
                        (YML_NESTED1, YML_NESTED2, EXPECTED_STYLISH),
                        (YML_NESTED1, JSON_NESTED2, EXPECTED_STYLISH)])
def test_diff_recursive_stylish(test_input1, test_input2, expected):
    assert generate_diff(test_input1, test_input2, 'stylish') == expected


@pytest.mark.parametrize("test_input1,test_input2,expected", [
                        (JSON_NESTED1, JSON_NESTED2, EXPECTED_PLAIN),
                        (YML_NESTED1, YML_NESTED2, EXPECTED_PLAIN),
                        (YML_NESTED1, JSON_NESTED2, EXPECTED_PLAIN)])
def test_diff_recursive_plain(test_input1, test_input2, expected):
    assert generate_diff(test_input1, test_input2, 'plain') == expected


@pytest.mark.parametrize("test_input1,test_input2,expected", [
                        (JSON_NESTED1, JSON_NESTED2, EXPECTED_JSON),
                        (YML_NESTED1, YML_NESTED2, EXPECTED_JSON),
                        (YML_NESTED1, JSON_NESTED2, EXPECTED_JSON)])
def test_diff_recursive_json(test_input1, test_input2, expected):
    assert generate_diff(test_input1, test_input2, 'json') == expected
