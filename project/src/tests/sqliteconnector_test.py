import unittest
import time
from connectors.sqliteconnector import SQLiteConnector
from constants import TIME_EXP


class TestSQLiteDbConnector(unittest.TestCase):
    def setUp(self):
        self.config = {'name': 'Tester', 'connector': 'SQLiteConnector',
                       'uri': 'config/demo_db.sqlite',
                       'transformations': {'format': 'records',
                                           'header': 'add names',
                                           'names': 'time,$VALUE,name',
                                           'pivot': 'yes',
                                           'time_format': 'milliseconds'
                       }}
        self.source = SQLiteConnector(**self.config)

    def test_constructor_saves_attributes(self):
        self.assertNotEqual(self.source, None)
        self.assertEqual(self.source._uri, 'config/demo_db.sqlite')

    def test_data_can_be_fetched_with_no_timespan(self):
        data = self.source.get_data('ruuvitags',
                                    {'time':'time','value':'humidity','name':'name'}, None, None)
        self.assertEqual(data.shape, (204,4))

    def test_data_can_be_fetched_with_timespan(self):
        timespan = time.time() - 1637413815.185 + TIME_EXP['hour'] # Mock 1-hour span in stale db
        data = self.source.get_data('ruuvitags',
                                    {'time':'time','value':'humidity','name':'name'}, None, timespan)
        self.assertEqual(data.shape, (32,4))
