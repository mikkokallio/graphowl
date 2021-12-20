import unittest
from confighandler import ConfigHandler
from dashboard import Dashboard


class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.loader = ConfigHandler('config/testdashboard.yaml')
        self.dummy_source = {'name':'Dummy','connector':'Connector','uri':'dummy','transformations':{}}
        self.dummy_graph = {'title':'Graph','connector':'Dummy','collection':'dummy',
                       'fields':{'time':'time','value':'dummy','name':'dummy'}, 'transformations':{}}
        self.dashboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '8 hours', '10 minutes',
                                   [self.dummy_source],
                                   [self.dummy_graph, self.dummy_graph, self.dummy_graph])

    def test_constructor_stores_correct_values(self):
        dashboard = Dashboard(**self.loader.load())
        self.assertEqual(dashboard.title, 'Statistics')
        self.assertEqual(dashboard.timespan, None)
        self.assertEqual(dashboard.interval, 120)
        self.assertEqual(dashboard.layout['x'], 2)
        self.assertEqual(dashboard.layout['y'], 2)
        self.assertEqual(len(dashboard._graphs), 4)
        self.assertEqual(len(dashboard._sources), 1)

    def test_parsing_negatives_returns_none(self):
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '-8 hours', '10 minutes', [], [])
        self.assertEqual(faulty_dboard.timespan, None)

    def test_parsing_zero_returns_none(self):
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '-8 hours', '0 min', [], [])
        self.assertEqual(faulty_dboard.interval, None)

    def test_parsing_decimals_returns_none(self):
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '-8 hours', '0.5 min', [], [])
        self.assertEqual(faulty_dboard.interval, None)

    def test_parsing_nonsense_returns_none(self):
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '019 xxxse', '0 min', [], [])
        self.assertEqual(faulty_dboard.timespan, None)
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', 'abc suxxx', '0 min', [], [])
        self.assertEqual(faulty_dboard.timespan, None)

    def test_parsing_too_many_args_returns_none(self):
        faulty_dboard = Dashboard('Dummy', {'x':2,'y':2}, 'no', '0124 xxx mins', '0 min', [], [])
        self.assertEqual(faulty_dboard.timespan, None)

    def test_nonpositive_dimension_becomes_1(self):
        faulty_dboard = Dashboard('Dummy', {'x':-1,'y':-2}, 'no', '0124 xxx mins', '0 min', [], [])
        self.assertEqual(faulty_dboard.layout['x'], 1)
        self.assertEqual(faulty_dboard.layout['y'], 1)

    def test_nonsense_dimension_becomes_1(self):
        faulty_dboard = Dashboard('Dummy', {'x':'x','y':'y'}, 'no', '0124 xxx mins', '0 min', [], [])
        self.assertEqual(faulty_dboard.layout, {'x':1, 'y':1})

    def test_load_all_gets_data(self):
        data = self.dashboard.load_all()
        self.assertEqual(len(data),3)
