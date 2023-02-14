import json
import yaml
from pathlib import Path

YAML = {'.yaml', '.yml'}


def _normalize_unchanged(val):
    '''Convert unchanged parts of the compared dicts to the diff dict format
    '''
    if type(val) is dict:
        return {key: {'': _normalize_unchanged(value)}
                for key, value in val.items()
                }
    return val


def _get_diff_dict(first_dict: dict, second_dict: dict) -> dict:
    '''Compare two dictionaries and return the difference as a dictionary
    '''
    first_dict_keys = first_dict.keys()
    second_dict_keys = second_dict.keys()
    all_keys = first_dict_keys | second_dict_keys
    diff = {}

    for key in sorted(all_keys):
        diff[key] = {}
        # key is in the both dicts and the values are the same
        if key in first_dict_keys and key in second_dict_keys and \
           first_dict.get(key) == second_dict.get(key):
            diff[key][''] = _normalize_unchanged(first_dict[key])
            continue

        # was non-terminal, become non-terminal
        if type(fd := first_dict.get(key)) is dict and \
           type(sd := second_dict.get(key)) is dict:
            diff[key][''] = _get_diff_dict(fd, sd)
            continue

        # was (non-)terminal become non-existent or
        # was terminal,      become non terminal or
        # was non terminal,  become terminal or
        # was terminal,      become terminal but with a different value
        if key in first_dict_keys:
            diff[key]['-'] = _normalize_unchanged(first_dict[key])

        # was non existent  become (non-)terminal or
        # was terminal,     become non-terminal or
        # was non-terminal, become terminal or
        # was terminal,     become terminal but with a different value
        if key in second_dict_keys:
            diff[key]['+'] = _normalize_unchanged(second_dict[key])

    return diff


def _convert_json_to_dict(file_name: str) -> dict:
    path_to_file = Path(file_name)
    if path_to_file.suffix in YAML:
        return yaml.safe_load(open(path_to_file))
    return json.load(open(path_to_file))


def gen_diff(first_file: str, second_file: str, formatter) -> str:
    '''Compare two json/yml files and return the difference in the text format

    Args:
        first_file - name of the first json/yaml file to be compared
        second_file - name of the second json/yaml file to be compared
        formatter - function used to format the difference report
    '''
    first_dict = _convert_json_to_dict(first_file)
    second_dict = _convert_json_to_dict(second_file)

    diff = _get_diff_dict(first_dict, second_dict)

    return formatter(diff)
