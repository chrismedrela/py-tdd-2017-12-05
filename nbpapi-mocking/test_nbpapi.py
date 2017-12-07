import datetime
import unittest

import mock

import nbpapi


class GetTablesTests(unittest.TestCase):
    @mock.patch('nbpapi.request', autospec=True)
    def test_it_works(self, request_mock):
        bytes = b'''\xef\xbb\xbfc001z170102\r\nh001z170102\r\na001z170102'''
        request_mock.urlopen.return_value.read.return_value = bytes

        got = nbpapi.get_tables()
        expected = ['c001z170102', 'h001z170102', 'a001z170102']
        self.assertEqual(got, expected)

        request_mock.urlopen.assert_called_once_with(
            'http://www.nbp.pl/kursy/xml/dir.txt')


# GetTableNameTests - before refactoring

class GetTableNameTests(unittest.TestCase):
    @mock.patch('nbpapi.get_tables', autospec=True)
    def test_should_return_valid_table_name(self, get_tables_mock):
        get_tables_mock.return_value = [
            'a001z170102',
            'b002z170103',
            'a002z170103',
        ]
        date = datetime.date(2017, 1, 3)

        got = nbpapi.get_table_name(date)
        expected = 'a002z170103'
        self.assertEqual(got, expected)

        get_tables_mock.assert_called_once_with()

    @mock.patch('nbpapi.get_tables', autospec=True)
    def test_should_return_None_for_missing_tables(self, get_tables_mock):
        get_tables_mock.return_value = [
            'a001z170102',
            'b002z170103',
            'a002z170103',
        ]
        date = datetime.date(2017, 1, 1)

        got = nbpapi.get_table_name(date)
        expected = None
        self.assertEqual(got, expected)

        get_tables_mock.assert_called_once_with()


# GetTableNameTests - after refactoring

class GetTableNameTests(unittest.TestCase):
    def test_should_return_valid_table_name(self):
        self._test_get_table_name(
            date=datetime.date(2017, 1, 3),
            expected='a002z170103')

    def test_should_return_None_for_missing_tables(self):
        self._test_get_table_name(
            date=datetime.date(2017, 1, 1),
            expected=None)

    @mock.patch('nbpapi.get_tables', autospec=True)
    def _test_get_table_name(self, get_tables_mock, date, expected):
        get_tables_mock.return_value = [
            'a001z170102',
            'b002z170103',
            'a002z170103',
        ]

        got = nbpapi.get_table_name(date)
        self.assertEqual(got, expected)

        get_tables_mock.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
