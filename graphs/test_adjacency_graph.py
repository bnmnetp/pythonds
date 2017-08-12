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
        filename = 'graphs/adjacency_graph.txt'
        with open(filename, 'r') as input_file:
            for raw_line in input_file:
                line = raw_line.split()
                if len(line) == 1:
                    src = line[0]
                elif len(line) == 2:
                    self._graph.add_edge(src, line[0], int(line[1]))

    def test_len(self):
        '''Testing len() method'''
        self.assertEqual(len(self._graph), 7)

    def test_vertex_str(self):
        '''Testing vertex str() method'''
        with patch('sys.stdout', new=StringIO()) as output:
            for vertex in self._graph:
                print(vertex.key, end=' ')
        self.assertEqual(sorted(output.getvalue().strip().split()),
                         ['t', 'u', 'v', 'w', 'x', 'y', 'z'])

    def tearDown(self):
        '''Tearing down'''
        del self._graph

if __name__ == '__main__':
    unittest.main(verbosity=2)
