# html2csv

`html2csv` is a utility that extracts tables from HTML documents and converts them to CSV format, written in Python.

## Usage

```
usage: html2csv [-h] [-o [OUTPUT]] [-e ENGINE] [input [input ...]]

Convert HTML table to CSV format.

positional arguments:
  input                 input sources (files, URLs, etc., default: standard
                        input)

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        output target (default: standard output)
  -e ENGINE, --engine ENGINE
                        HTML parser engine (default: html.parser or lxml if
                        installed)
```

## Author and Contact

Wentao Han (wentao.han@gmail.com)
