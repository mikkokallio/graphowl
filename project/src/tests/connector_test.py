import unittest
from datetime import datetime
from connectors.connector import Connector


class TestConnector(unittest.TestCase):
    def setUp(self):
        self.source = Connector('mock/mock', {})

    def test_constructor_creates_connector(self):
        self.assertNotEqual(self.source, None)

    def test_get_data(self):
        self.assertNotEqual(self.source.get_data(), None)
