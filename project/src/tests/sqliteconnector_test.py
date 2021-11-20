import unittest
import sqlite3
from connectors.sqliteconnector import SQLiteConnector
from constants import TIME_EXP
import time


class TestSQLiteDbConnector(unittest.TestCase):
    def setUp(self):
        self.source = SQLiteConnector('Tester', 'test.sqlite')

    def test_constructor_saves_attributes(self):
        self.assertNotEqual(self.source, None)
        self.assertEqual(self.source.name, 'Tester')
        self.assertEqual(self.source.uri, 'test.sqlite')
    
    def test_get_data_works_with_no_timespan(self):
        pass

    def test_data_is_fetched_from_database(self):
        pass
        #collname = 'dummycoll'
        #self.collection = self.source._db[collname]
        #now = int(time.time() * 1000)
        #objs = [
        #    {'_id':'61903f31274919d5fbb5728e','time':now,'temperature':'3.78','moisture':"65.25","pressure":"1003.23","name":"balcony"},
        #    {'_id':'61903f5b274919d5fbb5728f','time':now-TIME_EXP['hour'],'temperature':'3.53','moisture':"65.63","pressure":"1003.12","name":"balcony"},
        #    {'_id':'61903f8e274919d5fbb57290','time':now-TIME_EXP['day'],'temperature':'2.99','moisture':"66.13","pressure":"1002.67","name":"balcony"},
        #    {'_id':'61903fd6274919d5fbb57291','time':now,'temperature':'24.21','moisture':'32.66',"pressure":"999.45","name":"kitchen"},
        #    {'_id':'6190401e274919d5fbb57292','time':now-TIME_EXP['hour'],'temperature':'24.17','moisture':"32.73","pressure":"999.64","name":"kitchen"},
        #    {'_id':'61904052274919d5fbb57293','time':now-TIME_EXP['day'],'temperature':'23.96','moisture':"32.32","pressure":"999.78","name":"kitchen"}
        #    ]
        #self.collection.insert_many(objs)
        #fields = { 'time': 'time', 'value': 'temperature', 'name': 'name'}

        #result = self.source.get_data(collname, fields, 2 * TIME_EXP['day'])
        #desired_result = {'balcony': ([now, now-TIME_EXP['hour'], now-TIME_EXP['day']], ['3.78', '3.53', '2.99']), 'kitchen': ([now, now-TIME_EXP['hour'], now-TIME_EXP['day']], ['24.21', '24.17', '23.96'])}

        #self.assertEqual(result, desired_result)
