import pytest
from os.path import abspath
from gendiff.gendiff import generate_diff
import tests


def build_fixture_path(file_name):
    return tests.FIXTURES_PATH + file_name


@pytest.mark.parametrize("test_input1,test_input2,expected,format", [
                        ('plain_file1.json', 'plain_file2.json', 'result_plain.txt', 'stylish'),
                        ('plain_filepath.yml', 'plain_filepath2.yaml', 'result_plain.txt', 'stylish'),
                        ('plain_filepath.yml', 'plain_file2.json', 'result_plain.txt', 'stylish'),
                        ('file1.json', 'file2.json', 'result_recursive.txt', 'stylish'),
                        ('file_yml1.yml', 'file_yml2.yml', 'result_recursive.txt', 'stylish'),
                        ('file_yml1.yml', 'file2.json', 'result_recursive.txt', 'stylish'),
                        ('file1.json', 'file2.json', 'result_recursive_plain.txt', 'plain'),
                        ('file_yml1.yml', 'file_yml2.yml', 'result_recursive_plain.txt', 'plain'),
                        ('file_yml1.yml', 'file2.json', 'result_recursive_plain.txt', 'plain'),
                        ('file1.json', 'file2.json', 'result_json.txt', 'json'),
                        ('file_yml1.yml', 'file_yml2.yml', 'result_json.txt', 'json'),
                        ('file_yml1.yml', 'file2.json', 'result_json.txt', 'json')])
def test_diff(test_input1, test_input2, expected, format):
    with open(abspath(build_fixture_path(expected)), 'r') as result:
        filepath1 = build_fixture_path(test_input1)
        filepath2 = build_fixture_path(test_input2)
        assert generate_diff(filepath1, filepath2, format) == result.read()
