'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''

import heapq
import sys


class Vertex:
    '''Graph vertex class'''
    def __init__(self, key):
        '''Create new vertex'''
        self._key = key
        self._neighbors = {}
        self._color = 'white'
        self._distance = sys.maxsize
        self._previous = None
        self._discovery_time = 0
        self._closing_time = 0

    def __lt__(self, other):
        '''Less than operator required for heapify'''
        return self.key < other.key

    def get_key(self):
        '''Get vertex key'''
        return self._key

    key = property(get_key)

    def get_neighbor(self, other):
        """Get one adjacent node (neighbor)"""
        return self._neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        '''Add neighbor'''
        self._neighbors[other] = weight

    def get_neighbors(self):
        '''Get all adjacent nodes (neighbors)'''
        return self._neighbors.keys()

    def get_color(self):
        '''Get vertex color'''
        return self._color

    def set_color(self, color):
        '''Set vertex color'''
        self._color = color

    color = property(get_color, set_color)

    def get_distance(self):
        '''Get distance'''
        return self._distance

    def set_distance(self, distance):
        '''Set distance'''
        self._distance = distance

    distance = property(get_distance, set_distance)

    def get_previous(self):
        '''Get previous'''
        return self._previous

    def set_previous(self, previous):
        '''Set previous'''
        self._previous = previous

    previous = property(get_previous, set_previous)

    def get_discovery_time(self):
        '''Get discovery time'''
        return self._discovery_time

    def set_discovery_time(self, discovery_time):
        '''Set discovery time'''
        self._discovery_time = discovery_time

    discovery_time = property(get_discovery_time, set_discovery_time)

    def get_closing_time(self):
        '''Get closing time'''
        return self._closing_time

    def set_closing_time(self, closing_time):
        '''Set closing time'''
        self._closing_time = closing_time

    closing_time = property(get_closing_time, set_closing_time)

    def __str__(self):
        return str(self._key) + \
                ":color " + self._color + \
                ":discovery_time " + str(self._discovery_time) + \
                ":closing_time " + str(self._closing_time) + \
                ":distance " + str(self._distance) + \
                ":previous \n\t[" + str(self._previous) + "]\n"


class Graph:
    '''Graph as an adjacency matrix'''
    def __init__(self):
        self._vertices = {}
        self._time = 0

    def __iter__(self):
        '''Iterator'''
        return iter(self._vertices.values())

    def size(self):
        '''Graph's size'''
        return len(self._vertices)

    def __len__(self):
        '''Graph's size'''
        return len(self._vertices)

    def __contains__(self, key):
        '''in operator override'''
        return key in self._vertices

    def get_vertex(self, key):
        '''Find the vertex in the graph named vert_key'''
        return self._vertices.get(key, None)

    def set_vertex(self, key):
        '''Add an instance of Vertex to the graph'''
        self._vertices[key] = Vertex(key)

    def add_edge(self, from_vertex, to_vertex, weight=0):
        '''Add a weighted and directed edge to the graph'''
        if from_vertex not in self._vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self._vertices:
            self.set_vertex(to_vertex)
        self._vertices[from_vertex].set_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        '''Return the list of all vertices in the graph'''
        return self._vertices.keys()

    def reset_distances(self):
        '''Reset distances to test Dijkstra's'''
        for vertex in self:
            vertex.set_distance(sys.maxsize)

    def bfs(self, start):
        '''Breadth First Search'''
        start.set_distance(0)
        start.set_previous(None)
        vert_queue = [start]
        while vert_queue:
            current_vert = vert_queue.pop(0)
            for neigh in current_vert.get_neighbors():
                if neigh.get_color() == 'white':
                    neigh.set_color('gray')
                    neigh.set_distance(current_vert.get_distance() + 1)
                    neigh.set_previous(current_vert)
                    vert_queue.append(neigh)
            current_vert.set_color('black')

    def dfs(self):
        '''Depth First search'''
        for vertex in self:
            if vertex.get_color() == 'white':
                self.dfs_visit(vertex)

    def dfs_visit(self, start):
        '''DFS helper function'''
        start.set_color('gray')
        self._time = self._time + 1
        start.set_discovery_time(self._time)
        for next_vertex in start.get_neighbors():
            if next_vertex.get_color() == 'white':
                next_vertex.set_previous(start)
                self.dfs_visit(next_vertex)
        start.set_color('black')
        self._time = self._time + 1
        start.set_closing_time(self._time)

    def traverse(self, src, dst):
        '''Traverse a graph'''
        path = []
        current = self.get_vertex(dst)
        while current:
            path.insert(0, current)
            current = current.get_previous()
        print('Path from {} to {} ({}): {}'.format(self.get_vertex(src).get_key(),
                                                   self.get_vertex(dst).get_key(),
                                                   self.get_vertex(dst).get_distance(),
                                                   ' '.join(v.get_key() for v in path)))

    def dijkstra(self, start):
        '''Dijkstra's shortest path algorithm'''
        start.set_distance(0)
        not_yet_visited = [[start.get_distance(), start]]
        heapq.heapify(not_yet_visited)
        while not_yet_visited:
            current_vertex = heapq.heappop(not_yet_visited)[1]
            for next_vertex in current_vertex.get_neighbors():
                new_distance = current_vertex.get_distance() + current_vertex.get_neighbor(next_vertex)
                if new_distance < next_vertex.get_distance():
                    next_vertex.set_distance(new_distance)
                    next_vertex.set_previous(current_vertex)
                    found = False
                    for vertex in not_yet_visited:
                        if vertex[1].get_key() == next_vertex.get_key():
                            vertex[0] = next_vertex.get_distance()
                            heapq.heapify(not_yet_visited)
                            found = True
                    if not found:
                        heapq.heappush(not_yet_visited, [next_vertex.get_distance(), next_vertex])
