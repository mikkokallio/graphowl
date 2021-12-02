import unittest
from graph import Graph
from connectors.connector import Connector


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sources = {'mocky': Connector('path')}
        self.orig = {'title': 'Example-Graph',
                 'connector': 'mocky',
                 'collection': 'metrics',
                 'fields': {'time': 'time', 'value': 'temperature', 'name': 'alias'}}
        self.graph = Graph(self.orig['title'], self.sources[self.orig['connector']],
                           self.orig['collection'], self.orig['fields'])

    def test_constructor_stores_attributes(self):
        self.assertEqual(self.graph.title, 'Example-Graph')
        self.assertEqual(type(self.graph.connector), Connector)
        self.assertEqual(self.graph.collection, 'metrics')
        self.assertEqual(self.graph.fields['time'], 'time')
        self.assertEqual(self.graph.fields['value'], 'temperature')
        self.assertEqual(self.graph.fields['name'], 'alias')

    def test_load_gets_data(self):
        data = self.graph.load()
        self.assertEqual(type(data), dict)
