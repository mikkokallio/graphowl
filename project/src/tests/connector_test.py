import unittest
from datetime import datetime
from connectors.connector import Connector


class TestConnector(unittest.TestCase):
    def setUp(self):
        self.source = Connector('mock/mock')

    def test_constructor_creates_connector(self):
        self.assertNotEqual(self.source, None)

    def test_transform_works_correctly(self):
        data = [{'time': 1000, 'value': 3.78, 'name': 'balcony'},
                {'time': 1010, 'value': 3.53, 'name': 'balcony'},
                {'time': 1020, 'value': 2.99, 'name': 'balcony'},
                {'time': 1000, 'value': 24.21, 'name': 'kitchen'},
                {'time': 1010, 'value': 24.17, 'name': 'kitchen'},
                {'time': 1020, 'value': 23.96, 'name': 'kitchen'}]
        desired_output = {'balcony': ([datetime(1970, 1, 1, 2, 0, 1),
                                       datetime(1970, 1, 1, 2, 0, 1, 10000),
                                       datetime(1970, 1, 1, 2, 0, 1, 20000)],
                                      [3.78, 3.53, 2.99]),
                          'kitchen': ([datetime(1970, 1, 1, 2, 0, 1),
                                       datetime(1970, 1, 1, 2, 0, 1, 10000),
                                       datetime(1970, 1, 1, 2, 0, 1, 20000)],
                                      [24.21, 24.17, 23.96])}
        output = self.source._transform(data)
        self.assertEqual(output, desired_output)

    def test_get_data(self):
        self.assertNotEqual(self.source.get_data(), None)
