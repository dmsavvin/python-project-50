import argparse
from gendiff.jsondiff import get_json_diff

FORMATS = ['json', 'plain']


def run_cli(argv=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', action='store',
                        choices=FORMATS, help='set format of output',
                        default=FORMATS[0], metavar='FORMAT')
    parser.add_argument('first_file_name')
    parser.add_argument('second_file_name')
    args = parser.parse_args(argv)

    if args.format == 'json':
        print(get_json_diff(args.first_file_name, args.second_file_name))


if __name__ == '__main__':
    run_cli(['-h'])
