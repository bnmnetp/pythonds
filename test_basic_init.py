'''
Testing the basic __init__ file
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from basic import Deque, OrderedList, Queue, Stack, UnorderedList


class TestBasicsInit(unittest.TestCase):
    '''Testing the basic __init__ file'''

    def setUp(self):
        '''Setting up'''
        self._stack = Stack()
        self._queue = Queue()
        self._deque = Deque()
        self._olist = OrderedList()
        self._ulist = UnorderedList()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self._stack.is_empty())
        self.assertTrue(self._queue.is_empty())
        self.assertTrue(self._deque.is_empty())
        self.assertTrue(self._olist.is_empty())
        self.assertTrue(self._ulist.is_empty())

if __name__ == '__main__':
    unittest.main()
