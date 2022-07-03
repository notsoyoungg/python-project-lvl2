import json
import os.path
from gendifff.modules import make_diff


dict1 = json.load(open(os.path.abspath('./gendifff/tests/fixtures/file1.json')))
dict2 = json.load(open(os.path.abspath('./gendifff/tests/fixtures/file2.json')))


def test_make_diff():
    assert make_diff.generate_diff(dict1, dict2) == "{ \n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"
