#!/usr/bin/env python3
"""
Testing the Graph module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.graphs.adjacency_graph import Graph


class TestGraphMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.graph = Graph()
        filename = "tests/graphs/test_adjacency_graph.txt"
        with open(filename, "r") as input_file:
            for raw_line in input_file:
                line = raw_line.split()
                if len(line) == 1:
                    src = line[0]
                elif len(line) == 2:
                    self.graph.add_edge(src, line[0], int(line[1]))

    def test_len(self):
        """Testing len() method"""
        assert len(self.graph) == 7

    def test_vertex_str(self, capsys):
        """Testing vertex str() method"""
        self.graph.reset_distances(255)
        for vertex in self.graph:
            print(vertex)
            out, err = capsys.readouterr()
            assert out.strip() == (
                vertex.key + "    | white  |  255   |   0    |   0    | None"
            )

    def test_traverse(self, capsys):
        """Testing graph traversal output"""
        expected_result_from_t = {
            "u": [["t", "u"], 2],
            "v": [["t", "v"], 4],
            "w": [["t", "u", "w"], 5],
            "x": [["t", "v", "x"], 7],
            "y": [["t", "y"], 7],
            "z": [["t", "v", "x", "z"], 15],
        }
        self.graph.reset_distances()
        start_vertex = "t"
        self.graph.dijkstra(self.graph.get_vertex(start_vertex))
        for vertex in self.graph.get_vertices() - {start_vertex}:
            self.graph.traverse(start_vertex, vertex)
            out, err = capsys.readouterr()
            assert out.strip() == "Path from {} to {} ({}): {}".format(
                start_vertex,
                vertex,
                expected_result_from_t[vertex][1],
                " ".join(expected_result_from_t[vertex][0]),
            )

    def test_dijkstra(self):
        """Testing Dijkstra's shortest path algorithm"""
        expected_result_from_t = {
            "u": ("t", 2),
            "v": ("t", 4),
            "w": ("u", 5),
            "x": ("v", 7),
            "y": ("t", 7),
            "z": ("x", 15),
        }
        self.graph.reset_distances()
        start_vertex = "t"
        self.graph.dijkstra(self.graph.get_vertex(start_vertex))
        for vertex in self.graph.get_vertices() - {start_vertex}:
            assert (
                self.graph.get_vertex(vertex).previous.key
                == expected_result_from_t[vertex][0]
            )
            assert (
                self.graph.get_vertex(vertex).distance
                == expected_result_from_t[vertex][1]
            )

    def test_bellman_ford(self):
        """Testing Bellman-Ford shortest path algorithm"""
        expected_result_from_t = {
            "u": ("t", 2),
            "v": ("t", 4),
            "w": ("u", 5),
            "x": ("v", 7),
            "y": ("t", 7),
            "z": ("x", 15),
        }
        self.graph.reset_distances()
        start_vertex = "t"
        self.graph.bellman_ford(self.graph.get_vertex(start_vertex))
        for vertex in self.graph.get_vertices() - {start_vertex}:
            assert (
                self.graph.get_vertex(vertex).previous.key
                == expected_result_from_t[vertex][0]
            )
            assert (
                self.graph.get_vertex(vertex).distance
                == expected_result_from_t[vertex][1]
            )

    def test_bellman_ford_error(self):
        """Testing Bellman-Ford shortest path algorithm exception"""
        self.err_graph = Graph()
        self.err_graph.add_edge("t", "u", -2)
        self.err_graph.add_edge("u", "v", -3)
        self.err_graph.add_edge("v", "t", -4)
        self.err_graph.reset_distances()
        start_vertex = "t"
        with pytest.raises(ValueError):
            self.err_graph.bellman_ford(self.err_graph.get_vertex(start_vertex))

    def test_prim(self):
        """Testing Prim's spanning tree algorithm"""
        expected_result_from_t = {
            "u": ("t", 2),
            "v": ("u", 3),
            "w": ("u", 3),
            "x": ("v", 3),
            "y": ("x", 6),
            "z": ("x", 8),
        }
        self.graph.reset_distances(255)
        start_vertex = "t"
        self.graph.prim(self.graph.get_vertex(start_vertex))
        for vertex in self.graph.get_vertices() - {start_vertex}:
            assert (
                self.graph.get_vertex(vertex).previous.key
                == expected_result_from_t[vertex][0]
            )
            assert (
                self.graph.get_vertex(vertex).distance
                == expected_result_from_t[vertex][1]
            )

    def test_bfs(self):
        """Testing Breadth first search"""
        expected_result_from_t = {
            "t": 0,
            "u": 1,
            "v": 1,
            "w": 2,
            "x": 2,
            "y": 1,
            "z": 2,
        }
        start_vertex = "t"
        self.graph.bfs(self.graph.get_vertex(start_vertex))
        for vertex in self.graph:
            assert vertex.get_distance() == expected_result_from_t[vertex.key]

    def test_dfs(self):
        """Testing Depth first search"""
        # TODO: Come up with a more robust test
        self.graph.dfs()
        for vertex in self.graph:
            if vertex.discovery_time == 1:
                assert vertex.closing_time == 14


if __name__ == "__main__":
    pytest.main(["test_adjacency_graph.py"])
