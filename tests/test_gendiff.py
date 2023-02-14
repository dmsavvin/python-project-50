import json
import pytest
import dictdiffer
import gendiff.gendiff as gd
import tests.test_suits as ts


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
    assert gd.generate_diff(first_file, second_file, 'stylish') == \
        expected


@pytest.mark.parametrize("test_input,expected", ts.GEN_PLAIN_DIFF_TS)
def test_gen_plain_diff(test_input, expected):
    first_file, second_file = test_input
    assert gd.generate_diff(first_file, second_file, 'plain') == \
        expected


@pytest.mark.parametrize("test_input,expected", ts.GEN_JSON_DIFF_TS)
def test_gen_json_diff(test_input, expected):
    first_file, second_file = test_input
    generated_json_diff = gd.generate_diff(first_file, second_file, 'json')
    generated_json_diff_dict = json.loads(generated_json_diff)
    expected_json_diff_dict = json.loads(expected)
    assert not list(dictdiffer.diff(generated_json_diff_dict,
                                    expected_json_diff_dict))
