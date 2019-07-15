import unittest

from html2csv import Converter


class ConverterTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert(self):
        html_doc = '''\
<table>
<tr>
<th>A</th>
<th>B</th>
</tr>
<tr>
<td>1</td>
<td>2</td>
</tr>
</table>
'''
        output = self.converter.convert(html_doc)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0][0], '''\
A,B\r
1,2\r
'''
        )


if __name__ == '__main__':
    unittest.main()
