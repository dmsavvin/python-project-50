import argparse as ap
from gendiff.jsondiff import get_json_diff

FORMATS = ['plain', 'json']


def run_cli():
    parser = ap.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', action='store',
                        choices=FORMATS, help='set format of output',
                        default=FORMATS[0], metavar='FORMAT')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    # Do something with the first_file and the second_file
    # print(f'Here we are doing something with the {args.first_file}'
    #       f' and the {args.second_file}')
    # print(f'{args=}')
    # print(args.format)
    if args.format == 'json':
        print(get_json_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    run_cli()
