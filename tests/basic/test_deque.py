'''
Testing the Deque module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..')))


import unittest
from pythonds3.basic.deque import Deque


class TestDequeMethods(unittest.TestCase):
    '''Testing the Deque module'''

    def setUp(self):
        '''Setting up'''
        self._deque = Deque()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self._deque.is_empty())
        self._deque.add_front(42)
        self.assertFalse(self._deque.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self._deque.size(), 0)
        self._deque.add_front(42)
        self.assertEqual(self._deque.size(), 1)

    def test_add_front(self):
        '''Testing add_front() method'''
        self._deque.add_front(42)
        self.assertEqual(self._deque.size(), 1)

    def test_add_rear(self):
        '''Testing add_rear() method'''
        self._deque.add_rear(42)
        self.assertEqual(self._deque.size(), 1)

    def test_remove_front(self):
        '''Testing remove_front() method'''
        self._deque.add_front(42)
        self.assertEqual(self._deque.remove_front(), 42)
        self.assertTrue(self._deque.is_empty())

    def test_remove_rear(self):
        '''Testing remove_rear() method'''
        self._deque.add_rear(42)
        self.assertEqual(self._deque.remove_rear(), 42)
        self.assertTrue(self._deque.is_empty())

if __name__ == '__main__':
    unittest.main()
