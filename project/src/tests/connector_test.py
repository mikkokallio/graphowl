import unittest
from connectors.connector import Connector


class TestConnector(unittest.TestCase):
    def setUp(self):
        self.source = Connector('dummy', 'mock/mock')

    def test_constructor_creates_connector(self):
        self.assertNotEqual(self.source, None)
    
    def test_transform_works_correctly(self):
        input = [{'time': 1000, 'value': 3.78, 'name': 'balcony'}, {'time': 1010, 'value': 3.53, 'name': 'balcony'}, {'time': 1020, 'value': 2.99, 'name': 'balcony'}, {'time': 1000, 'value': 24.21, 'name': 'kitchen'}, {'time': 1010, 'value': 24.17, 'name': 'kitchen'}, {'time': 1020, 'value': 23.96, 'name': 'kitchen'}]
        desired_output = {'balcony': ([1000, 1010, 1020], [3.78, 3.53, 2.99]), 'kitchen': ([1000, 1010, 1020], [24.21, 24.17, 23.96])}
        output = self.source._transform(input)
        self.assertEqual(output, desired_output)

    def test_get_data(self):
        pass
