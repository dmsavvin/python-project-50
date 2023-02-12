import json
import yaml
from pathlib import Path

YAML = {'.yaml', '.yml'}
CONV_TBL = {'True': 'true',
            'False': 'false',
            'None': 'none'
            }


def _convert_json_to_dict(file_name: str) -> dict:
    path_to_file = Path(file_name)
    if path_to_file.suffix in YAML:
        return yaml.safe_load(open(path_to_file))
    return json.load(open(path_to_file))


def _norm_val(val):
    '''Convert keys of a dict to the ('', key) pairs
    '''
    if type(val) is dict:
        return {('', key): _norm_val(value)
                for key, value in val.items()
                }
    return val


def _get_dict_diff(first_dict: dict, second_dict: dict) -> dict:
    '''Compare two dictionaries and return the difference
    '''
    all_keys = first_dict.keys() | second_dict.keys()
    diff = {}

    for key in sorted(all_keys):
        # None == None situation is impossible hence key is in both
        # dicts and value is the same
        if first_dict.get(key) == second_dict.get(key):
            diff[('', key)] = _norm_val(first_dict[key])
            continue

        # was non terminal, becomes non terminal
        if type(fd := first_dict.get(key)) is dict and \
           type(sd := second_dict.get(key)) is dict:
            diff[('', key)] = _get_dict_diff(fd, sd)
            continue

        #                   becomes non existent or
        # was terminal,     becomes non terminal or
        # was non terminal, becomes terminal or
        # was terminal,     becomes terminal but with a different value
        if first_dict.get(key) is not None:
            diff[('-', key)] = _norm_val(first_dict[key])

        # was non existent or
        # was terminal,     becomes non terminal or
        # was non terminal, becomes terminal or
        # was terminal,     becomes terminal but with a different value
        if second_dict.get(key) is not None:
            diff[('+', key)] = _norm_val(second_dict[key])

    return diff


def _format_diff(diff, init_ind=0, incr_ind=2, sym_fld_len=2) -> str:
    '''Convert diff dict to a string

    Args:
        diff - dict to be converted to a string
        init_ind - initial part of an indent (use in recursive call to
            specify the indent of the parent)
        incr_ind - incremental indent between adjacent levels
        sym_field_len - length of the field for a symbol before key
    Example:
        ......................key1: {
        |                    |            +...............key2: value 2
        |                    |            |              |
        +----init_ind--------+--incr_ind--+--symbol_len--+
    '''
    indent = init_ind + incr_ind
    res = []

    res.append('{')

    for key in diff:
        value = diff[key]
        symbol, _key = key
        if type(value) is dict:
            res.append(f'{" " * indent}{symbol:<{sym_fld_len}}{_key}: '
                       f'{_format_diff(value, init_ind=indent+sym_fld_len)}'
                       )
        else:
            value = CONV_TBL[str(value)] if str(value) in CONV_TBL else value
            res.append(f'{" " * indent}{symbol:<{sym_fld_len}}{_key}: {value}')

    res.append(f'{" " * init_ind}' '}')

    return '\n'.join(res)


def get_json_diff(first_file_name: str, second_file_name: str) -> str:
    '''Compare two json files and return the difference
    '''
    first_dict = _convert_json_to_dict(first_file_name)
    second_dict = _convert_json_to_dict(second_file_name)

    diff = _get_dict_diff(first_dict, second_dict)

    return _format_diff(diff)
