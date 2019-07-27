# html2csv

`html2csv` is a utility that extracts tables from HTML documents and converts them to CSV format, written in Python.

## Usage

```
usage: html2csv [-h] [-o [OUTPUT_FILE]] [-e ENGINE]
                [input_file [input_file ...]]

Convert HTML table to CSV format.

positional arguments:
  input_file            input files (default: standard input)

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        output file (default: standard output)
  -e ENGINE, --engine ENGINE
                        HTML parser engine (default: html.parser or lxml if
                        installed)
```

## Author and Contact

Wentao Han (wentao.han@gmail.com)
