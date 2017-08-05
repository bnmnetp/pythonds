'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''
# queue.py


class Queue(object):
    '''Queue implementation as a list'''
    def __init__(self):
        '''Create new queue'''
        self.__items = []

    def is_empty(self):
        '''Check if the queue is empty'''
        return self.__items == []

    def enqueue(self, item):
        '''Add an item to the queue'''
        self.__items.insert(0, item)

    def dequeue(self):
        '''Remove an item from the queue'''
        return self.__items.pop()

    def size(self):
        '''Get the number of items in the queue'''
        return len(self.__items)
