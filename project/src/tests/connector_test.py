import unittest
from connectors.connector import Connector
import pandas


class TestConnector(unittest.TestCase):
    def setUp(self):
        self.source = Connector('mock/mock', {})

    def test_constructor_creates_connector(self):
        self.assertNotEqual(self.source, None)

    def test_get_data(self):
        self.assertTrue(isinstance(self.source.get_data(), pandas.DataFrame))
