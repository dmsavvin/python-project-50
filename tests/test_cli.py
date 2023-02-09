import pytest
from gendiff.cli import run_cli
from tests.const import HELP_MESSAGE, TEST_SUITE


@pytest.mark.parametrize("test_input,expected",
                         [(['-h'], HELP_MESSAGE), (['--help'], HELP_MESSAGE)])
def test_run_cli_help(capsys, test_input, expected):
    with pytest.raises(SystemExit) as e:
        run_cli(test_input)

    out, err = capsys.readouterr()

    assert out == HELP_MESSAGE
    assert e.type == SystemExit
    assert e.value.code == 0


@pytest.mark.parametrize("test_input,expected", TEST_SUITE)
def test_run_cli(capsys, test_input, expected):
    first_file_name, second_file_name = test_input

    run_cli(['-f', 'json', first_file_name, second_file_name])
    out_json, err = capsys.readouterr()

    run_cli([first_file_name, second_file_name])
    out_default, err = capsys.readouterr()

    assert out_json == expected
    assert out_default == expected
