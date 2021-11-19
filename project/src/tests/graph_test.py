import unittest
from unittest.mock import patch
from graph import Graph
from connector import Connector


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sources = {'mocky': Connector('mocky')}
        self.orig = {'title': 'Example-Graph', 
                 'connector': 'mocky', 
                 'collection': 'metrics', 
                 'fields': {'time': 'time', 'value': 'temperature', 'name': 'alias'}}
        self.graph = Graph(self.orig['title'], self.sources[self.orig['connector']], self.orig['collection'], self.orig['fields'])

    def test_constructor_stores_attributes(self):
        self.assertEqual(self.graph.title, 'Example-Graph')
        self.assertEqual(type(self.graph.connector), Connector)
        self.assertEqual(self.graph.collection, 'metrics')
        self.assertEqual(self.graph.fields['time'], 'time')
        self.assertEqual(self.graph.fields['value'], 'temperature')
        self.assertEqual(self.graph.fields['name'], 'alias')

    def test_asdict_returns_the_same_dict(self):
        restored = self.graph.asdict()
        self.assertEqual(self.orig, restored)
    
    def test_load_gets_data(self):
        self.graph.load()