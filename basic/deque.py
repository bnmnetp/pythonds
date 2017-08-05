'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''
# deque.py


class Deque(object):
    '''Queue implementation as a list'''
    def __init__(self):
        '''Create new deque'''
        self.__items = []

    def is_empty(self):
        '''Check if the deque is empty'''
        return self.__items == []

    def add_front(self, item):
        '''Add an item to the front of the deque'''
        self.__items.append(item)

    def add_rear(self, item):
        '''Add an item to the rear of the deque'''
        self.__items.insert(0, item)

    def remove_front(self):
        '''Remove an item from the front of the deque'''
        return self.__items.pop()

    def remove_rear(self):
        '''Remove an item from the rear of the deque'''
        return self.__items.pop(0)

    def size(self):
        '''Get the number of items in the deque'''
        return len(self.__items)
