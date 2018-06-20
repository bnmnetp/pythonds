'''
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''


class Stack(object):
    '''Stack implementation as a list'''
    def __init__(self):
        '''Create new stack'''
        self._items = []

    def is_empty(self):
        '''Check if the stack is empty'''
        return not bool(self._items)

    def push(self, item):
        '''Add an item to the stack'''
        self._items.append(item)

    def pop(self):
        '''Remove an item from the stack'''
        return self._items.pop()

    def peek(self):
        '''Get the value of the top item in the stack'''
        return self._items[-1]

    def size(self):
        '''Get the number of items in the stack'''
        return len(self._items)
