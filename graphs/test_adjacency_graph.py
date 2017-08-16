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

    def test_dijkstra(self):
        '''Testing Dijkstra's shortest path algorithm'''
        expected_result_from_t = {'u': [['t', 'u'], 2],
                                  'v': [['t', 'v'], 4],
                                  'w': [['t', 'u', 'w'], 5],
                                  'x': [['t', 'v', 'x'], 7],
                                  'y': [['t', 'y'], 7],
                                  'z': [['t', 'v', 'x', 'z'], 15]
                                 }
        self._graph.reset_distances()
        start_vertex = 't'
        self._graph.dijkstra(self._graph.get_vertex(start_vertex))
        for vertex in self._graph.get_vertices() - {start_vertex}:
            with patch('sys.stdout', new=StringIO()) as output:
                self._graph.traverse(start_vertex, vertex)
            self.assertEqual(output.getvalue().strip(),
                             'Path from {} to {} ({}): {}'.format(start_vertex,
                                                                  vertex,
                                                                  expected_result_from_t[vertex][1],
                                                                  ' '.join(expected_result_from_t[vertex][0])))

    def test_bfs(self):
        '''Testing Breadth first search'''
        expected_result_from_t = {'u': [['t', 'u'], 1],
                                  'v': [['t', 'v'], 1],
                                  'w': [['t', 'u', 'w'], 2],
                                  'x': [['t', 'y', 'x'], 2],
                                  'y': [['t', 'y'], 1],
                                  'z': [['t', 'y', 'z'], 2]
                                 }
        start_vertex = 't'
        self._graph.bfs(self._graph.get_vertex(start_vertex))
        for vertex in self._graph.get_vertices() - {start_vertex}:
            with patch('sys.stdout', new=StringIO()) as output:
                self._graph.traverse(start_vertex, vertex)
            self.assertEqual(output.getvalue().strip(),
                             'Path from {} to {} ({}): {}'.format(start_vertex,
                                                                  vertex,
                                                                  expected_result_from_t[vertex][1],
                                                                  ' '.join(expected_result_from_t[vertex][0])))

    def test_dfs(self):
        '''Testing Depth first search'''
        expected_result_from_t = {'t': (1, 14),
                                  'u': (2, 13),
                                  'v': (7, 8),
                                  'w': (3, 12),
                                  'x': (4, 11),
                                  'y': (6, 9),
                                  'z': (5, 10)
                                 }
        start_vertex = 't'
        self._graph.dfs_visit(self._graph.get_vertex(start_vertex))
        for vertex in self._graph:
            if vertex.get_color() == 'white':
                self._graph.dfs_visit(vertex)
        for vertex in self._graph.get_vertices():
            with patch('sys.stdout', new=StringIO()) as output:
                print('Time of {} is {}/{}'.format(self._graph.get_vertex(vertex).get_key(),
                                                   self._graph.get_vertex(vertex).get_discovery_time(),
                                                   self._graph.get_vertex(vertex).get_closing_time()))
            self.assertEqual(output.getvalue().strip(),
                             'Time of {} is {}/{}'.format(vertex,
                                                          expected_result_from_t[vertex][0],
                                                          expected_result_from_t[vertex][1]))

    def tearDown(self):
        '''Tearing down'''
        del self._graph

if __name__ == '__main__':
    unittest.main(verbosity=2)
