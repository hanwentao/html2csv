import argparse
import sys

from . import Converter


def main():
    parser = argparse.ArgumentParser(description='Convert HTML table to CSV format.')
    parser.add_argument('input_file', nargs='*', type=argparse.FileType('r'), default=[sys.stdin])
    parser.add_argument('-o', '--output-file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    converter = Converter()
    for input_file in args.input_file:
        output = converter.convert(input_file.read())
        for csv_string, _ in output:
            args.output_file.write(csv_string)


if __name__ == '__main__':
    sys.exit(main())
