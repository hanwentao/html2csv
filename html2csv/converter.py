import csv
import io

import bs4


class Converter:

    def __init__(self, engine='lxml', **kwargs):
        self.engine = engine
        self.params = kwargs

    def convert(self, html_doc):
        soup = bs4.BeautifulSoup(html_doc, self.engine)
        output = []
        for table_num, table in enumerate(soup.find_all('table')):
            csv_string = io.StringIO()
            csv_writer = csv.writer(csv_string)
            for tr in table.find_all('tr'):
                row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
                csv_writer.writerow(row)
            table_attrs = dict(num=table_num)
            output.append((csv_string.getvalue(), table_attrs))
        return output
