'''
Testing the Graph module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from pythonds3.graphs.adjacency_graph import Graph


class TestGraphMethods(unittest.TestCase):
    '''Testing the Graph module'''
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
        self._graph.reset_distances(255)
        # print('{:^8}|{:^8}|{:^8}|{:^8}|{:^8}| {}'.format('key','color', 'distance', 'discovrd', 'closed', 'previous'))
        for vertex in self._graph:
            with patch('sys.stdout', new=StringIO()) as output:
                print(vertex)
            self.assertEqual(output.getvalue().strip(), vertex.key + '    | white  |  255   |   0    |   0    | None')

    def test_traverse(self):
        '''Testing graph traversal output'''
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

    def test_dijkstra(self):
        '''Testing Dijkstra's shortest path algorithm'''
        expected_result_from_t = {'u': ('t', 2),
                                  'v': ('t', 4),
                                  'w': ('u', 5),
                                  'x': ('v', 7),
                                  'y': ('t', 7),
                                  'z': ('x', 15)
                                  }
        self._graph.reset_distances()
        start_vertex = 't'
        self._graph.dijkstra(self._graph.get_vertex(start_vertex))
        for vertex in self._graph.get_vertices() - {start_vertex}:
            self.assertEqual(self._graph.get_vertex(vertex).previous.key, expected_result_from_t[vertex][0])
            self.assertEqual(self._graph.get_vertex(vertex).distance, expected_result_from_t[vertex][1])

    def test_bellman_ford(self):
        '''Testing Bellman-Ford shortest path algorithm'''
        expected_result_from_t = {'u': ('t', 2),
                                  'v': ('t', 4),
                                  'w': ('u', 5),
                                  'x': ('v', 7),
                                  'y': ('t', 7),
                                  'z': ('x', 15)
                                  }
        self._graph.reset_distances()
        start_vertex = 't'
        self._graph.bellman_ford(self._graph.get_vertex(start_vertex))
        for vertex in self._graph.get_vertices() - {start_vertex}:
            self.assertEqual(self._graph.get_vertex(vertex).previous.key, expected_result_from_t[vertex][0])
            self.assertEqual(self._graph.get_vertex(vertex).distance, expected_result_from_t[vertex][1])

    def test_bellman_ford_error(self):
        '''Testing Bellman-Ford shortest path algorithm exception'''
        self._graph.add_edge('t', 'u', -2)
        self._graph.add_edge('u', 'v', -3)
        self._graph.add_edge('v', 't', -4)
        self._graph.reset_distances()
        start_vertex = 't'
        with self.assertRaises(ValueError):
            self._graph.bellman_ford(self._graph.get_vertex(start_vertex))

    def test_prim(self):
        '''Testing Prim's spanning tree algorithm'''
        expected_result_from_t = {'u': ('t', 2),
                                  'v': ('u', 3),
                                  'w': ('u', 3),
                                  'x': ('v', 3),
                                  'y': ('x', 6),
                                  'z': ('x', 8)
                                  }
        self._graph.reset_distances(255)
        start_vertex = 't'
        self._graph.prim(self._graph.get_vertex(start_vertex))
        for vertex in self._graph.get_vertices() - {start_vertex}:
            self.assertEqual(self._graph.get_vertex(vertex).previous.key, expected_result_from_t[vertex][0])
            self.assertEqual(self._graph.get_vertex(vertex).distance, expected_result_from_t[vertex][1])

    def test_bfs(self):
        '''Testing Breadth first search'''
        expected_result_from_t = {'t': 0, 'u': 1, 'v': 1, 'w': 2, 'x': 2, 'y': 1, 'z': 2}
        start_vertex = 't'
        self._graph.bfs(self._graph.get_vertex(start_vertex))
        for vertex in self._graph:
            self.assertEqual(vertex.get_distance(), expected_result_from_t[vertex.key])

    def test_dfs(self):
        '''Testing Depth first search'''
        # TODO: Come up with a more robust test
        self._graph.dfs()
        for vertex in self._graph:
            if vertex.discovery_time == 1:
                self.assertEqual(vertex.closing_time, 14)

if __name__ == '__main__':
    unittest.main()
