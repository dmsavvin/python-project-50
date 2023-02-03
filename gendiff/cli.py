import argparse as ap


def cli():
    parser = ap.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    # Do something with the first_file and the second_file
    print(f'Here we are doing something with the {args.first_file}'
          f' and the {args.second_file}')


if __name__ == '__main__':
    cli()
