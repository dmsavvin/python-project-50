import argparse
from gendiff.gendiff import gen_diff
from gendiff.formatters.stylish import get_stylish_diff
from gendiff.formatters.plain import get_plain_diff

FORMATS = ['json', 'plain']


def run_cli(argv=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', action='store',
                        choices=FORMATS, help='set format of output',
                        default=FORMATS[0], metavar='FORMAT')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args(argv)

    if args.format == 'json':
        print(gen_diff(args.first_file, args.second_file, get_stylish_diff))
    else:
        print(gen_diff(args.first_file, args.second_file, get_plain_diff))


if __name__ == '__main__':
    run_cli(['-h'])
