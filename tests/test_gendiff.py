import pytest
import gendiff.gendiff as gd
import tests.test_suits as ts
from gendiff.formatters.stylish import get_stylish_diff
from gendiff.formatters.plain import get_plain_diff


@pytest.mark.parametrize("test_input,expected", ts.CONVERT_JSON_TO_DICT_TS)
def test_convert_json_to_dict(test_input, expected):
    assert gd._convert_json_to_dict(test_input) == expected


@pytest.mark.parametrize("test_input,expected", ts.GET_DIFF_DICT_TS)
def test_get_diff_dict(test_input, expected):
    first_dict, second_dict = test_input
    assert gd._get_diff_dict(first_dict, second_dict) == expected


@pytest.mark.parametrize("test_input,expected", ts.GEN_STYLISH_DIFF_TS)
def test_gen_stylish_diff(test_input, expected):
    first_file, second_file = test_input
    assert gd.gen_diff(first_file, second_file, get_stylish_diff) == \
        expected


@pytest.mark.parametrize("test_input,expected", ts.GEN_PLAIN_DIFF_TS)
def test_gen_plain_diff(test_input, expected):
    first_file, second_file = test_input
    assert gd.gen_diff(first_file, second_file, get_plain_diff) == \
        expected
