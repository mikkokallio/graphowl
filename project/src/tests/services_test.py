import unittest
from services import resolve_path


class TestServices(unittest.TestCase):
    def setUp(self):
        self.data = {'root': {'node1': {'child1': 'test', 'child2': 'text'}, 'node2': {'child1': 111, 'child2': 222}}}

    def test_resolve_path_read(self):
        read = resolve_path(['root', 'node1', 'child2'], self.data)
        self.assertEqual(read, 'text')

    def test_resolve_path_write(self):
        resolve_path(['root', 'node1', 'child1'], self.data, 'changed')
        self.assertEqual(self.data['root']['node1']['child1'], 'changed')

    def test_resolve_path_write_number(self):
        resolve_path(['root', 'node2', 'child1'], self.data, 666)
        self.assertEqual(self.data['root']['node2']['child1'], 666)
