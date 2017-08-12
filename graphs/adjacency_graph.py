'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''

import sys


class Graph:
    '''Graph as an adjacency matrix'''
    def __init__(self):
        self._vertices = {}
        self._time = 0

    def get_vertex(self, key):
        '''Find the vertex in the graph named vert_key'''
        return self._vertices.get(key, None)

    def set_vertex(self, key):
        '''Add an instance of Vertex to the graph'''
        self._vertices[key] = Vertex(key)

    def __contains__(self, key):
        '''in operator override'''
        return key in self._vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        '''Add a new, weighted, directed edge to the graph that connects two vertices'''
        if from_vertex not in self._vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self._vertices:
            self.set_vertex(to_vertex)
        self._vertices[from_vertex].set_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        '''Return the list of all vertices in the graph'''
        return self._vertices.keys()

    def __iter__(self):
        '''Iterator'''
        return iter(self._vertices.values())

    def size(self):
        '''Graph's size'''
        return len(self._vertices)

    def __len__(self):
        '''Graph's size'''
        return len(self._vertices)

    def read_file(self, filename):
        '''Read the graph from a file'''
        with open(filename, 'r') as input_file:
            for raw_line in input_file:
                line = raw_line.split()
                if len(line) == 1:
                    src = line[0]
                elif len(line) == 2:
                    self.add_edge(src, line[0], int(line[1]))


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

    def get_key(self):
        '''Get vertex key'''
        return self._key

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

    previoua = property(get_previous, set_previous)

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
                ":_closing_time " + str(self._closing_time) + \
                ":_distance " + str(self._distance) + \
                ":_previous \n\t[" + str(self._previous)+ "]\n"
