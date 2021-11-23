import unittest
from confighandler import ConfigHandler
from dashboard import Dashboard


class TestConfigHandler(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')

    def test_constructor_stores_filepath(self):
        self.assertEqual(self.loader.filepath, 'config/testdashboard.yaml')

    def test_handler_load_creates_dashboard(self):
        dashboard = self.loader.load()
        self.assertEqual(type(dashboard), Dashboard)
