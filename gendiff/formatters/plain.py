from gendiff.formatters.consts import CONV_TBL


def _normalize_for_plain_diff(val):
    '''Normalize value to be placed to the plain difference report
    '''
    if type(val) is dict:
        return '[complex value]'
    if type(val) is str:
        return f"'{val}'"
    return CONV_TBL[str(val)] if str(val) in CONV_TBL else val


def _get_plain_diff_as_list(diff: dict, prefix: str = None) -> list:
    '''Convert diff dict to the plain difference report stored as list
    '''
    prefix = [] if prefix is None else prefix
    res = []
    for key, symbols in diff.items():
        prop = prefix + [key]
        prop_str = '.'.join(prop)
        if symbols.keys() == {'+'}:
            res.append(f"Property '{prop_str}' was added with value: "
                       f"{_normalize_for_plain_diff(symbols['+'])}")
        if symbols.keys() == {'-'}:
            res.append(f"Property '{prop_str}' was removed")
        if symbols.keys() == {'-', '+'}:
            res.append(f"Property '{prop_str}' was updated. From "
                       f"{_normalize_for_plain_diff(symbols['-'])} to "
                       f"{_normalize_for_plain_diff(symbols['+'])}")
        if symbols.keys() == {''} and type(symbols['']) is dict:
            res.extend(_get_plain_diff_as_list(symbols[''], prop))
    return res


def get_plain_diff(diff: dict) -> str:
    '''Convert diff dict to the plain difference report
    '''
    return '\n'.join(_get_plain_diff_as_list(diff))
