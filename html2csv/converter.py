import csv
import io

import bs4


def detect_engine():
    try:
        import lxml
    except ImportError:
        engine = 'html.parser'
    else:
        engine = 'lxml'
    return engine


class Converter:

    def __init__(self, **kwargs):
        engine = kwargs.get('engine')
        if engine is None:
            self.engine = detect_engine()
        else:
            self.engine = engine
        self.params = kwargs

    def convert_to_list(self, html_doc):
        soup = bs4.BeautifulSoup(html_doc, self.engine)
        tables = []
        for table in soup.find_all('table'):
            table = []
            for tr in table.find_all('tr'):
                row = [''.join(cell.stripped_strings)
                       for cell in tr.find_all(['td', 'th'])]
                table.append(row)
            tables.append(table)
        return tables

    def convert_to_csv(self, html_doc):
        tables = self.convert_to_list(html_doc)
        output = []
        for table_num, table in enumerate(tables):
            csv_string = io.StringIO()
            csv_writer = csv.writer(csv_string)
            for row in table:
                csv_writer.writerow(row)
            table_attrs = dict(num=table_num)
            output.append((csv_string.getvalue(), table_attrs))
        return output

    def convert(self, html_doc):
        return self.convert_to_csv(html_doc)
