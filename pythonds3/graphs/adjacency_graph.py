#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

import heapq
import sys


class Vertex:
    """Graph vertex class"""

    def __init__(self, key):
        """Create new vertex"""
        self._key = key
        self._neighbors = {}
        self._color = "white"
        self._distance = sys.maxsize
        self._previous = None
        self._discovery_time = 0
        self._closing_time = 0

    def __lt__(self, other):
        """Less than operator required for heapify"""
        return self.key < other.key

    def get_key(self):
        """Get vertex key"""
        return self._key

    key = property(get_key)

    def get_neighbor(self, other):
        """Get the distance (edge weight) to an adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        """Set the distance (add an edge) to an adjacent node (neighbor)"""
        self._neighbors[other] = weight

    def get_neighbors(self):
        """Get all adjacent nodes (neighbors)"""
        return self._neighbors.keys()

    def get_color(self):
        """Get vertex color"""
        return self._color

    def set_color(self, color):
        """Set vertex color"""
        self._color = color

    color = property(get_color, set_color)

    def get_distance(self):
        """Get distance"""
        return self._distance

    def set_distance(self, distance):
        """Set distance"""
        self._distance = distance

    distance = property(get_distance, set_distance)

    def get_previous(self):
        """Get previous"""
        return self._previous

    def set_previous(self, previous):
        """Set previous"""
        self._previous = previous

    previous = property(get_previous, set_previous)

    def get_discovery_time(self):
        """Get discovery time"""
        return self._discovery_time

    def set_discovery_time(self, discovery_time):
        """Set discovery time"""
        self._discovery_time = discovery_time

    discovery_time = property(get_discovery_time, set_discovery_time)

    def get_closing_time(self):
        """Get closing time"""
        return self._closing_time

    def set_closing_time(self, closing_time):
        """Set closing time"""
        self._closing_time = closing_time

    closing_time = property(get_closing_time, set_closing_time)

    def __str__(self):
        return "{:^8}|{:^8}|{:^8}|{:^8}|{:^8}| {}".format(
            self._key,
            self._color,
            self._distance,
            self._discovery_time,
            self._closing_time,
            self._previous,
        )


class Graph:
    """Graph as an adjacency matrix"""

    def __init__(self):
        self._vertices = {}
        self._edges = {}
        self._time = 0

    def __iter__(self):
        """Iterator"""
        return iter(self._vertices.values())

    def size(self):
        """Graph's size"""
        return len(self._vertices)

    def __len__(self):
        """Graph's size"""
        return len(self._vertices)

    def __contains__(self, key):
        """in operator override"""
        return key in self._vertices

    def get_vertex(self, key):
        """Find the vertex in the graph named vert_key"""
        return self._vertices.get(key, None)

    def set_vertex(self, key):
        """Add an instance of Vertex to the graph"""
        self._vertices[key] = Vertex(key)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """Add a weighted and directed edge to the graph"""
        if from_vertex not in self._vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self._vertices:
            self.set_vertex(to_vertex)
        self._vertices[from_vertex].set_neighbor(self._vertices[to_vertex], weight)
        self._edges[(from_vertex, to_vertex)] = weight

    def get_vertices(self):
        """Return the list of all vertices in the graph"""
        return self._vertices.keys()

    def get_edges(self):
        """Return the list of all edges in the graph"""
        return self._edges.keys()

    def reset_distances(self, default_distance=sys.maxsize):
        """Reset distances to test Dijkstra's"""
        for vertex in self:
            vertex.distance = default_distance

    def bfs(self, start):
        """Breadth First Search"""
        start.distance = 0
        start.previous = None
        vert_queue = [start]
        while vert_queue:
            current_vert = vert_queue.pop(0)
            for neigh in current_vert.get_neighbors():
                if neigh.color == "white":
                    neigh.color = "gray"
                    neigh.distance = current_vert.distance + 1
                    neigh.previous = current_vert
                    vert_queue.append(neigh)
            current_vert.color = "black"

    def dfs(self):
        """Depth First search"""
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start):
        """DFS helper function"""
        start.color = "gray"
        self._time = self._time + 1
        start.discovery_time = self._time
        for next_vertex in start.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.set_previous(start)
                self.dfs_visit(next_vertex)
        start.color = "black"
        self._time = self._time + 1
        start.closing_time = self._time

    def traverse(self, src, dst):
        """Traverse a graph"""
        path = []
        current = self.get_vertex(dst)
        while current:
            path.append(current)
            current = current.previous
        print(
            "Path from {} to {} ({}): {}".format(
                self.get_vertex(src).key,
                self.get_vertex(dst).key,
                self.get_vertex(dst).distance,
                " ".join(vertex.key for vertex in reversed(path)),
            )
        )

    def dijkstra(self, start):
        """Dijkstra's shortest path algorithm"""
        start.distance = 0
        not_yet_visited = [[start.distance, start]]
        heapq.heapify(not_yet_visited)
        while not_yet_visited:
            current_vertex = heapq.heappop(not_yet_visited)[1]
            for next_vertex in current_vertex.get_neighbors():
                new_distance = current_vertex.distance + current_vertex.get_neighbor(
                    next_vertex
                )
                if new_distance < next_vertex.distance:
                    next_vertex.distance = new_distance
                    next_vertex.previous = current_vertex
                    found = False
                    for vertex in not_yet_visited:
                        if vertex[1].key == next_vertex.key:
                            vertex[0] = next_vertex.distance
                            heapq.heapify(not_yet_visited)
                            found = True
                    if not found:
                        heapq.heappush(
                            not_yet_visited, [next_vertex.distance, next_vertex]
                        )

    def bellman_ford(self, start):
        """Bellman-Ford shortest path algorithm"""
        start.distance = 0
        for _ in range(len(self._vertices)):
            for edge in self._edges:
                if (
                    self.get_vertex(edge[0]).distance + self._edges[edge]
                    < self.get_vertex(edge[1]).distance
                ):
                    self.get_vertex(edge[1]).distance = (
                        self.get_vertex(edge[0]).distance + self._edges[edge]
                    )
                    self.get_vertex(edge[1]).previous = self.get_vertex(edge[0])
        for edge in self._edges:
            if (
                self.get_vertex(edge[0]).distance + self._edges[edge]
                < self.get_vertex(edge[1]).distance
            ):
                raise ValueError("Graph contains a negative-weight cycle")

    def prim(self, start):
        """Prim's spanning tree algorithm"""
        start.distance = 0
        not_in_a_tree = [[vertex.distance, vertex] for vertex in self]
        heapq.heapify(not_in_a_tree)
        while not_in_a_tree:
            current_vertex = heapq.heappop(not_in_a_tree)[1]
            for next_vertex in current_vertex.get_neighbors():
                new_distance = current_vertex.get_neighbor(next_vertex)
                if (
                    any(item[1] == next_vertex for item in not_in_a_tree)
                    and new_distance < next_vertex.distance
                ):
                    next_vertex.previous = current_vertex
                    next_vertex.distance = new_distance
                    for item in not_in_a_tree:
                        if item[1] == next_vertex:
                            item[0] = new_distance
                            heapq.heapify(not_in_a_tree)
                            break
