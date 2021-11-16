import unittest
from unittest.mock import patch
import mongomock
from mongodbconnector import MongoDbConnector


class TestMongoDbConnector(unittest.TestCase):
    def setUp(self):
        with patch('pymongo.MongoClient', mongomock.MongoClient):
            self.source = MongoDbConnector('uri', 'cert', 'db')

    def test_constructor_creates_connector_with_client_and_db(self):
        self.assertNotEqual(self.source, None)
        self.assertNotEqual(self.source._client, None)
        self.assertNotEqual(self.source._db, None)

    def test_transform_works_correctly(self):
        input = [{'time': 1000, 'value': 3.78, 'name': 'balcony'}, {'time': 1010, 'value': 3.53, 'name': 'balcony'}, {'time': 1020, 'value': 2.99, 'name': 'balcony'}, {'time': 1000, 'value': 24.21, 'name': 'kitchen'}, {'time': 1010, 'value': 24.17, 'name': 'kitchen'}, {'time': 1020, 'value': 23.96, 'name': 'kitchen'}]
        desired_output = {'balcony': ([1000, 1010, 1020], [3.78, 3.53, 2.99]), 'kitchen': ([1000, 1010, 1020], [24.21, 24.17, 23.96])}
        output = self.source._transform(input)
        self.assertEqual(output, desired_output)

    def test_data_is_fetched_from_database(self):
        collname = 'dummycoll'
        self.collection = self.source._db[collname]
        objs = [
            {'_id':'61903f31274919d5fbb5728e','time':'1000','temperature':'3.78','moisture':"65.25","pressure":"1003.23","name":"balcony"},
            {'_id':'61903f5b274919d5fbb5728f','time':'1010','temperature':'3.53','moisture':"65.63","pressure":"1003.12","name":"balcony"},
            {'_id':'61903f8e274919d5fbb57290','time':'1020','temperature':'2.99','moisture':"66.13","pressure":"1002.67","name":"balcony"},
            {'_id':'61903fd6274919d5fbb57291','time':'1000','temperature':'24.21','moisture':'32.66',"pressure":"999.45","name":"kitchen"},
            {'_id':'6190401e274919d5fbb57292','time':'1010','temperature':'24.17','moisture':"32.73","pressure":"999.64","name":"kitchen"},
            {'_id':'61904052274919d5fbb57293','time':'1020','temperature':'23.96','moisture':"32.32","pressure":"999.78","name":"kitchen"}
            ]
        self.collection.insert_many(objs)
        fields = { 'time': 'time', 'value': 'temperature', 'name': 'name'}

        result = self.source.get_data(collname, fields)
        #desired_result = {'balcony': ([1000, 1010, 1020], [3.78, 3.53, 2.99]), 'kitchen': ([1000, 1010, 1020], [24.21, 24.17, 23.96])}
        desired_result = {'balcony': (['1000', '1010', '1020'], ['3.78', '3.53', '2.99']), 'kitchen': (['1000', '1010', '1020'], ['24.21', '24.17', '23.96'])}

        self.assertEqual(result, desired_result)
