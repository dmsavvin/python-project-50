import argparse
from gendiff.gendiff import generate_diff
from gendiff.formatters.stylish import get_stylish_diff
from gendiff.formatters.plain import get_plain_diff
from gendiff.formatters.fjson import get_json_diff

FORMATS = ['stylish', 'plain', 'json']
FORMATTERS = {'stylish': get_stylish_diff,
              'plain': get_plain_diff,
              'json': get_json_diff}


def run_cli(argv=None):
    '''Run command line interface for the gen_diff function'''
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', action='store',
                        choices=FORMATS, help='set format of output',
                        default=FORMATS[0], metavar='FORMAT')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args(argv)

    print(generate_diff(args.first_file, args.second_file,
                        FORMATTERS[args.format]))


if __name__ == '__main__':
    run_cli(['-h'])
