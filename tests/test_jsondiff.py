import pytest
import gendiff.jsondiff as jd
import tests.test_suits as ts


@pytest.mark.parametrize("test_input,expected", ts.CONVERT_JSON_TO_DICT_TS)
def test_convert_json_to_dict(test_input, expected):
    assert jd._convert_json_to_dict(test_input) == expected


@pytest.mark.parametrize("test_input,expected", ts.NORM_VAL_TS)
def test_norm_val(test_input, expected):
    assert jd._norm_val(test_input) == expected


@pytest.mark.parametrize("test_input,expected", ts.GET_DICT_DIFF_TS)
def test_get_dict_diff(test_input, expected):
    first_dict, second_dict = test_input
    assert jd._get_dict_diff(first_dict, second_dict) == expected


@pytest.mark.parametrize("test_input,expected", ts.FORMAT_DIFF_TS)
def test_format_diff(test_input, expected):
    assert jd._format_diff(test_input) == expected


@pytest.mark.parametrize("test_input,expected", ts.GET_JSON_DIFF_TS)
def test_get_json_diff(test_input, expected):
    first_file_name, second_file_name = test_input
    assert jd.get_json_diff(first_file_name, second_file_name) == \
        expected.strip(' \t\n\b')
