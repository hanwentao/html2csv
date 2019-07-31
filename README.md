# html2csv

[![Build Status](https://travis-ci.com/hanwentao/html2csv.svg?branch=master)](https://travis-ci.com/hanwentao/html2csv)

`html2csv` is a utility that extracts tables from HTML documents and converts them to CSV format, written in Python.

[![asciicast](https://asciinema.org/a/259747.svg)](https://asciinema.org/a/259747)

## Setup

Python 3 is required (version >=3.6).  Install `html2csv` by `pip`.

```
pip install html-to-csv
```

Yes, the package name is `html-to-csv` due to collision ;-)

## Examples

Input from the standard input, and output to the standard output.

    html2csv

Input from a file, and output to the standard output.

    html2csv example.html

Input from files, and output to a file.

    html2csv example1.html example2.html -o output.csv

Input from the network, and output to the standard output.

    html2csv http://example.com

## Usage

```
usage: html2csv [-h] [-o [OUTPUT]] [-e ENGINE] [-V] [input [input ...]]

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
  -V, --version         display version
```

## Author and Contact

Wentao Han (wentao.han@gmail.com)
