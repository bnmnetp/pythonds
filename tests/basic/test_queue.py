'''
Testing the Queue module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..')))

import unittest
from pythonds3.basic.queue import Queue


class TestQueueMethods(unittest.TestCase):
    '''Testing the Queue module'''

    def setUp(self):
        '''Setting up'''
        self._queue = Queue()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self._queue.is_empty())
        self._queue.enqueue(42)
        self.assertFalse(self._queue.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self._queue.size(), 0)
        self._queue.enqueue(42)
        self.assertEqual(self._queue.size(), 1)

    def test_enqueue(self):
        '''Testing enqueue() method'''
        self._queue.enqueue(42)
        self.assertEqual(self._queue.size(), 1)

    def test_dequeue(self):
        '''Testing dequeue() method'''
        self._queue.enqueue(42)
        self.assertEqual(self._queue.dequeue(), 42)
        self.assertTrue(self._queue.is_empty())

if __name__ == '__main__':
    unittest.main()
