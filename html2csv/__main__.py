import argparse
import pathlib
import sys

import requests

from . import Converter, __version__


def main():
    parser = argparse.ArgumentParser(description='Convert HTML table to CSV format.')
    parser.add_argument('input',
        help='input sources (files, URLs, etc., default: standard input)',
        nargs='*',
        default=['-'],
    )
    parser.add_argument('-o', '--output',
        help='output target (default: standard output)',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout,
    )
    parser.add_argument('-e', '--engine',
        help='HTML parser engine (default: html.parser or lxml if installed)',
    )
    parser.add_argument('-V', '--version',
        action='store_true',
        help='display version',
    )
    args = parser.parse_args()
    if args.version:
        print(f'{__package__} {__version__}')
        return
    converter = Converter(**vars(args))
    for input_source in args.input:
        if not input_source or input_source == '-':
            html_doc = sys.stdin.read()
        else:
            path = pathlib.Path(input_source)
            if path.exists():
                html_doc = path.read_text()
            else:
                response = requests.get(input_source)
                html_doc = response.text
        output = converter.convert(html_doc)
        for csv_string, _ in output:
            args.output.write(csv_string)


if __name__ == '__main__':
    sys.exit(main())
