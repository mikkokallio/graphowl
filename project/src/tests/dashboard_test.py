import unittest
from unittest.mock import patch
from confighandler import ConfigHandler
from dashboard import Dashboard
from graph import Graph


class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')
        self.dummy_dashboard = Dashboard('Dummy', {'x':2,'y':2}, '8 hours', '10 minutes', [], [])

    def test_constructor_stores_correct_values(self):
        dashboard = self.loader.load()
        self.assertEqual(dashboard.title, 'Test')
        self.assertEqual(dashboard.timespan, 43200)
        self.assertEqual(dashboard.interval, 300)
        self.assertEqual(dashboard.layout['x'], 3)
        self.assertEqual(dashboard.layout['y'], 2)
        self.assertEqual(len(dashboard.graphs), 4)
        self.assertEqual(len(dashboard.sources), 1)
    
    def test_parsing_negatives_returns_none(self):
        result = self.dummy_dashboard.parse_time_config('-5 hours')
        self.assertEqual(result, None)

    def test_parsing_zero_returns_none(self):
        result = self.dummy_dashboard.parse_time_config('0 min')
        self.assertEqual(result, None)

    def test_parsing_decimals_returns_none(self):
        result = self.dummy_dashboard.parse_time_config('0.5 min')
        self.assertEqual(result, None)

    def test_parsing_nonsense_returns_none(self):
        result = self.dummy_dashboard.parse_time_config('019 xxxse')
        self.assertEqual(result, None)
        result = self.dummy_dashboard.parse_time_config('abc suxxx')
        self.assertEqual(result, None)
        result = self.dummy_dashboard.parse_time_config('0124 xxx mins')
        self.assertEqual(result, None)

    def test_parsing_too_many_args_returns_none(self):
        result = self.dummy_dashboard.parse_time_config('0124 xxxse mins')
        self.assertEqual(result, None)
    
    def test_layout_has_negative_or_zero_dimension(self):
        pass
