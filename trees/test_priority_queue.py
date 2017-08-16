'''
Testing the Priority Queue module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from priority_queue import PriorityQueue


class TestPriorityQueueMethods(unittest.TestCase):
    '''Testing the Priority Queue module'''

    def setUp(self):
        '''Setting up'''
        self._priority_queue = PriorityQueue()
        self._priority_queue.insert((2, 'x'))
        self._priority_queue.insert((3, 'y'))
        self._priority_queue.insert((5, 'z'))
        self._priority_queue.insert((6, 'a'))
        self._priority_queue.insert((4, 'd'))

    def test_delete(self):
        '''testing delete() method'''
        self.assertEqual(self._priority_queue.delete(), (2, 'x'))
        self.assertEqual(self._priority_queue.delete(), (3, 'y'))

    def test_decrease_key(self):
        '''Testing decrease_key() method'''
        self._priority_queue.change_priority(1, 'd')
        self.assertEqual(self._priority_queue.delete(), (1, 'd'))

if __name__ == '__main__':
    unittest.main()
