import unittest
from unittest.mock import patch
from datetime import datetime
import mongomock
from connectors.mongodbconnector import MongoDbConnector
from constants import TIME_EXP


class TestMongoDbConnector(unittest.TestCase):
    def setUp(self):
        self.config = {'name': 'Mongo', 'connector': 'MongoDbConnector', 'uri': 'mongodb://mock', 'cert': 'mock.pem', 'database': 'values'}
        with patch('pymongo.MongoClient', mongomock.MongoClient):
            self.source = MongoDbConnector(**self.config)

    def test_constructor_creates_connector(self):
        self.assertNotEqual(self.source, None)
        self.assertNotEqual(self.source._db, None)

    def test_data_is_fetched_from_database(self):
        collname = 'dummycoll'
        self.collection = self.source._db[collname]
        objs = [
            {'_id':'61903f31274919d5fbb5728e',
             'time':1638469814090,'temperature':'3.78','moisture':"65.25",
             "pressure":"1003.23","name":"balcony"},
            {'_id':'61903f5b274919d5fbb5728f',
             'time':1638469814090-TIME_EXP['hour'],'temperature':'3.53','moisture':"65.63",
             "pressure":"1003.12","name":"balcony"},
            {'_id':'61903f8e274919d5fbb57290',
             'time':1638469814090-TIME_EXP['day'],'temperature':'2.99','moisture':"66.13",
             "pressure":"1002.67","name":"balcony"},
            {'_id':'61903fd6274919d5fbb57291',
             'time':1638469814090,'temperature':'24.21','moisture':'32.66',
             "pressure":"999.45","name":"kitchen"},
            {'_id':'6190401e274919d5fbb57292',
             'time':1638469814090-TIME_EXP['hour'],'temperature':'24.17','moisture':"32.73",
             "pressure":"999.64","name":"kitchen"},
            {'_id':'61904052274919d5fbb57293',
             'time':1638469814090-TIME_EXP['day'],'temperature':'23.96','moisture':"32.32",
             "pressure":"999.78","name":"kitchen"}
            ]
        self.collection.insert_many(objs)
        fields = { 'time': 'time', 'value': 'temperature', 'name': 'name'}

        result = self.source.get_data(collname, fields, 2 * TIME_EXP['day'])
        desired_result = {'balcony': ([datetime(2021, 12, 2, 20, 30, 14, 90000),
                                       datetime(2021, 12, 2, 20, 30, 10, 490000),
                                       datetime(2021, 12, 2, 20, 28, 47, 690000)],
                                      ['3.78', '3.53', '2.99']),
                          'kitchen': ([datetime(2021, 12, 2, 20, 30, 14, 90000),
                                       datetime(2021, 12, 2, 20, 30, 10, 490000),
                                       datetime(2021, 12, 2, 20, 28, 47, 690000)],
                                      ['24.21', '24.17', '23.96'])}

        self.assertEqual(result, desired_result)
