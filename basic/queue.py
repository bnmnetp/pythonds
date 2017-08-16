'''
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''


class Queue(object):
    '''Queue implementation as a list'''
    def __init__(self):
        '''Create new queue'''
        self._items = []

    def is_empty(self):
        '''Check if the queue is empty'''
        return not bool(self._items)

    def enqueue(self, item):
        '''Add an item to the queue'''
        self._items.insert(0, item)

    def dequeue(self):
        '''Remove an item from the queue'''
        return self._items.pop()

    def size(self):
        '''Get the number of items in the queue'''
        return len(self._items)
