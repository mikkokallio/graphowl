import unittest
from confighandler import ConfigHandler
from dashboard import Dashboard


class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')
        dummy_source = {'name':'Dummy','connector':'Connector','uri':'dummy'}
        dummy_graph = {'title':'Graph','connector':'Dummy','collection':'dummy',
                       'fields':{'time':'time','value':'dummy','name':'dummy'}}
        self.dashboard = Dashboard('Dummy', {'x':2,'y':2}, '8 hours', '10 minutes',
                                         [dummy_source], [dummy_graph, dummy_graph, dummy_graph])

    def test_constructor_stores_correct_values(self):
        dashboard = Dashboard(**self.loader.load())
        self.assertEqual(dashboard.title, 'Test')
        self.assertEqual(dashboard._timespan, 43200)
        self.assertEqual(dashboard.interval, 300)
        self.assertEqual(dashboard.layout['x'], 3)
        self.assertEqual(dashboard.layout['y'], 2)
        self.assertEqual(len(dashboard._graphs), 4)
        self.assertEqual(len(dashboard._sources), 1)

    def test_parsing_negatives_returns_none(self):
        
        result = self.dashboard._parse_time_config('-5 hours')
        self.assertEqual(result, None)

    def test_parsing_zero_returns_none(self):
        result = self.dashboard._parse_time_config('0 min')
        self.assertEqual(result, None)

    def test_parsing_decimals_returns_none(self):
        result = self.dashboard._parse_time_config('0.5 min')
        self.assertEqual(result, None)

    def test_parsing_nonsense_returns_none(self):
        result = self.dashboard._parse_time_config('019 xxxse')
        self.assertEqual(result, None)
        result = self.dashboard._parse_time_config('abc suxxx')
        self.assertEqual(result, None)
        result = self.dashboard._parse_time_config('0124 xxx mins')
        self.assertEqual(result, None)

    def test_parsing_too_many_args_returns_none(self):
        result = self.dashboard._parse_time_config('0124 xxxse mins')
        self.assertEqual(result, None)

    def test_nonpositive_dimension_becomes_1(self):
        layout = {'x':-1, 'y':2}
        self.assertEqual(self.dashboard._validate_layout(layout), {'x':1, 'y':2})
        layout = {'x':1, 'y':-2}
        self.assertEqual(self.dashboard._validate_layout(layout), {'x':1, 'y':1})

    def test_nonsense_dimension_becomes_1(self):
        layout = {'x':'x', 'y':'y'}
        self.assertEqual(self.dashboard._validate_layout(layout), {'x':1, 'y':1})

    def test_load_all_gets_data(self):
        data = self.dashboard.load_all()
        self.assertEqual(len(data),3)
