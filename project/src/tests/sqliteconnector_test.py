import unittest
from connectors.sqliteconnector import SQLiteConnector
from constants import TIME_EXP
import time


class TestSQLiteDbConnector(unittest.TestCase):
    def setUp(self):
        self.config = {'name': 'Tester', 'connector': 'SQLiteConnector', 'uri': 'config/demo_db.sqlite'}
        self.source = SQLiteConnector(**self.config)

    def test_constructor_saves_attributes(self):
        self.assertNotEqual(self.source, None)
        self.assertEqual(self.source.name, 'Tester')
        self.assertEqual(self.source.uri, 'config/demo_db.sqlite')

    def test_asdict_converts_back_to_config(self):
        restored = self.source.asdict()
        self.assertEqual(restored, self.config)
    
    def test_data_can_be_fetched_with_no_timespan(self):
        data = self.source.get_data('ruuvitags', {'time':'time','value':'humidity','name':'name'}, None)
        self.assertEqual(len(data), 4)
        self.assertEqual(len(data['kitchen'][0]), 47)

    def test_data_can_be_fetched_with_timespan(self):
        timespan = time.time() - 1637413815.185 + TIME_EXP['hour'] # Mocking 1-hour span in a stale db
        data = self.source.get_data('ruuvitags', {'time':'time','value':'humidity','name':'name'},timespan)
        self.assertEqual(len(data['kitchen'][0]), 8)
