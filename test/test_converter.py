import pathlib
import unittest

from html2csv import Converter


def get_resource(relative_path):
    return pathlib.Path(__file__).parent / relative_path


class ConverterTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert(self):
        html_doc = get_resource('table.html').read_text()
        output = self.converter.convert(html_doc)
        csv_content = get_resource('table.csv').read_bytes()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0][0].encode(), csv_content)


if __name__ == '__main__':
    unittest.main()
