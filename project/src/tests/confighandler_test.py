import unittest
from unittest.mock import patch
import mongomock
from confighandler import ConfigHandler


class TestConfigHandler(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')

    def test_constructor_stores_filepath(self):
        self.assertEqual(self.loader.filepath, 'config/testdashboard.yaml')

    def test_dashboard_loads_details(self):
        dashboard = self.loader.load()
        self.assertEqual(dashboard.title, 'Test')
        self.assertEqual(dashboard.timespan, '12 hours')
        self.assertEqual(dashboard.interval, '5 minutes')
        self.assertEqual(dashboard.layout['x'], 3)
        self.assertEqual(dashboard.layout['y'], 2)
    
    def test_connectors_are_created_correctly(self):
        pass

    def test_graphs_are_created_correctly(self):
        pass
