from gendiff.formatters.consts import CONV_TBL


def get_stylish_diff(diff, init_ind=0, incr_ind=2, sym_len=2) -> str:
    '''Convert diff dict to the stylish difference report

    Args:
        diff - dict to be converted to a string
        init_ind - initial part of an indent (use in recursive call to
            specify the indent of the parent)
        incr_ind - incremental indent between adjacent levels
        sym_len - length of the field for a symbol before key

    Example:
        ......................key1:.{
        |....................|......('+'/'-'/'')............key2:.value2
        |                    |            |                |
        +----init_ind--------+--incr_ind--+---sym_fld_len--+
    '''
    indent = init_ind + incr_ind
    res = []
    res.append('{')
    for key in diff:
        for symbol in diff[key]:
            value = diff[key][symbol]
            if type(value) is dict:
                res.append(f'{" " * indent}{symbol:<{sym_len}}{key}: '
                           f'{get_stylish_diff(value, init_ind=indent+sym_len)}'
                           )
            else:
                value = CONV_TBL[str(value)] if str(value) in CONV_TBL \
                    else value
                res.append(f'{" " * indent}{symbol:<{sym_len}}'
                           f'{key}: {value}'
                           )
    res.append(f'{" " * init_ind}' '}')
    return '\n'.join(res)
