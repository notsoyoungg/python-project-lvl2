import pytest
from os.path import abspath
from gendiff.gendiff import generate_diff


JSON_FLAT1 = './tests/fixtures/plain_file1.json'
JSON_FLAT2 = './tests/fixtures/plain_file2.json'
JSON_NESTED1 = './tests/fixtures/file1.json'
JSON_NESTED2 = './tests/fixtures/file2.json'
YML_FLAT1 = './tests/fixtures/plain_filepath.yml'
YML_FLAT2 = './tests/fixtures/plain_filepath2.yaml'
YML_NESTED1 = './tests/fixtures/file_yml1.yml'
YML_NESTED2 = './tests/fixtures/file_yml2.yml'
EXPECTED_FLAT = open(abspath('./tests/fixtures/result_plain.txt'), 'r').read()
EXPECTED_STYLISH = open(abspath('./tests/fixtures/result_recursive.txt'
                                ), 'r').read()
EXPECTED_PLAIN = open(abspath('./tests/fixtures/result_recursive_plain.txt'
                              ), 'r').read()
EXPECTED_JSON = open(abspath('./tests/fixtures/result_json.txt'), 'r').read()


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
