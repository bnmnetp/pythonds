'''
Testing the basic __init__ file
Roman Yasinovskyy, 2017
'''

import unittest
from basic import *
#from pythonds.basic import *


class TestBasicsInit(unittest.TestCase):
    '''Testing the basic __init__ file'''

    def setUp(self):
        '''Setting up'''
        self.__stack = Stack()
        self.__queue = Queue()
        self.__deque = Deque()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self.__stack.is_empty())
        self.assertTrue(self.__queue.is_empty())
        self.assertTrue(self.__deque.is_empty())

    def tearDown(self):
        '''Tearing down'''
        del self.__stack
        del self.__queue
        del self.__deque

if __name__ == '__main__':
    unittest.main()
