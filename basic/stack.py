'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''
# stack.py


class Stack(object):
    '''Stack implementation as a list'''
    def __init__(self):
        '''Create new stack'''
        self.__items = []

    def is_empty(self):
        '''Check if the stack is empty'''
        return self.__items == []

    def push(self, item):
        '''Add an item to the stack'''
        self.__items.append(item)

    def pop(self):
        '''Remove an item from the stack'''
        return self.__items.pop()

    def peek(self):
        '''Get the value of the top item in the stack'''
        return self.__items[-1]

    def size(self):
        '''Get the number of items in the stack'''
        return len(self.__items)
