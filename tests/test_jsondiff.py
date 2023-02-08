from gendiff.jsondiff import _get_dict_diff, get_json_diff
import json

FIRST_FILE_NAME = './tests/fixtures/first.json'
with open(FIRST_FILE_NAME) as f:
    FIRST_DICT = json.load(f)

SECOND_FILE_NAME = './tests/fixtures/second.json'
with open(SECOND_FILE_NAME) as f:
    SECOND_DICT = json.load(f)

with open('./tests/fixtures/first-second-diff.txt') as f:
    FIRST_SECOND_DIFF = f.read()


def test_get_dict_diff():
    assert _get_dict_diff(FIRST_DICT, SECOND_DICT) == FIRST_SECOND_DIFF


def test_get_json_diff():
    assert get_json_diff(FIRST_FILE_NAME, SECOND_FILE_NAME) == FIRST_SECOND_DIFF
