import unittest
from confighandler import ConfigHandler
from dashboard import Dashboard


class TestConfigHandler(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')

    def test_constructor_stores_filepath(self):
        self.assertEqual(self.loader._filepath, 'config/testdashboard.yaml')

    def test_handler_loads_dashboard(self):
        config = self.loader.load()
        self.assertEqual(type(config), dict)
        dashboard = Dashboard(**config)
        self.assertEqual(type(dashboard), Dashboard)

    def test_handler_saves_dashboard(self):
        saver = ConfigHandler('src/tests/temp.yaml')
        config = self.loader.load()
        saver.save(config)
        saved_config = saver.load()
        self.assertEqual(saved_config, config)
