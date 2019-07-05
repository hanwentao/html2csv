import csv
import pathlib
import sys

import bs4


def main(args=sys.argv[1:]):
    html_path = pathlib.Path(args[0])
    output_path = html_path.parent
    basename = html_path.stem
    html_doc = html_path.read_text()
    soup = bs4.BeautifulSoup(html_doc, 'lxml')
    for table_num, table in enumerate(soup.find_all('table')):
        print(table_num, table.name, table.attrs)
        table_path = output_path / f'{basename}-{table_num}.csv'
        with open(table_path, 'w') as table_file:
            csv_writer = csv.writer(table_file)
            for tr in table.find_all('tr'):
                row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
                csv_writer.writerow(row)


if __name__ == '__main__':
    sys.exit(main())
