import json
import yaml
from pathlib import Path

YAML = {'.yaml', '.yml'}


def _get_dict_diff(first_dict: dict, second_dict: dict) -> str:
    '''Compare two dictionaries and show the difference

    Args:
        first_dict: first dictionary to be compared
        second_dict: second dictionary to be compared

    Returns:
        Multiline string that consists of the following lines:
        "  key: val" if key is in both dicts and it has the same value "val"
        "- key: val" if key is in the first dict with the value "val"
            but noexist or has the different value in the second dict
        "+ key: val" if key is in the second dict with the value "val"
            but noexist or has the different value in the first dict
        The returning string is sorted by "key".
    '''
    all_keys = first_dict.keys() | second_dict.keys()
    diff = {}

    for key in sorted(all_keys):
        # None == None situation is impossible hence key is in both
        # dicts and value is the same
        if first_dict.get(key) == second_dict.get(key):
            diff[f'  {key}'] = first_dict[key]
            continue

        # Key is in the first dict and it ether noexist or has different
        # value in the second dict
        if first_dict.get(key) is not None:
            diff[f'- {key}'] = first_dict[key]
        # Key is in the second dict and it ether noexist or has different
        # value in the first dict
        if second_dict.get(key) is not None:
            diff[f'+ {key}'] = second_dict[key]

    return diff


def get_json_diff(first_file: str, second_file: str) -> str:
    '''Compare two json files and show the difference

    Args:
        first_file: first file to be compared
        second_file: second file to be compared

    Returns:
        Multiline string that consists of the following lines:
        "  key: val" if key is in the both files and it has the same
            value "val"
        "- key: val" if key is in the first file with the value "val"
            but noexist or has the different value in the second file
        "+ key: val" if key is in the second file with the value "val"
            but noexist or has the different value in the first file
        The returning string is sorted by "key".
    '''
    path_to_first_file = Path(first_file)
    path_to_second_file = Path(second_file)

    if path_to_first_file.suffix in YAML:
        first_dict = yaml.safe_load(open(path_to_first_file))
    else:  # json
        first_dict = json.load(open(path_to_first_file))

    if path_to_second_file.suffix in YAML:
        second_dict = yaml.safe_load(open(path_to_second_file))
    else:  # json
        second_dict = json.load(open(path_to_second_file))

    return json.dumps(_get_dict_diff(first_dict, second_dict),
                      separators=('', ': '), indent=2
                      ).replace('"', '')
