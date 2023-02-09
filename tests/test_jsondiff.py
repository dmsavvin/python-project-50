import pytest
from gendiff.jsondiff import _get_dict_diff, get_json_diff
from tests.const import FIRST_DICT, SECOND_DICT, \
    TEST_SUITE, FIRST_SECOND_DICT_DIFF


def test_get_dict_diff():
    assert _get_dict_diff(FIRST_DICT, SECOND_DICT) == \
        FIRST_SECOND_DICT_DIFF


@pytest.mark.parametrize("test_input,expected", TEST_SUITE)
def test_get_json_diff(test_input, expected):
    first_file_name, second_file_name = test_input
    assert get_json_diff(first_file_name, second_file_name) == \
        expected.strip(' \t\n\b')
