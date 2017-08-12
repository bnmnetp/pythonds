'''
Testing the BinaryTree module
Roman Yasinovskyy, 2017
See https://stackoverflow.com/a/31281467 for testing output
'''

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from adjacency_graph import Graph


class TestAdjacencyGraphMethods(unittest.TestCase):
    '''Testing the Binary Heap module'''

    def setUp(self):
        '''Setting up'''
        self._graph = Graph()

    def test_makeGraph(self):
        '''Testing_make_graph'''
        self._graph.read_file("graphs/data_adjacency_graph.txt")
        self.assertEqual(self._graph.size(), 7)

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
