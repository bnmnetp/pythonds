'''
Testing the Queue module
Roman Yasinovskyy, 2017
'''

import unittest
import queue


class TestQueueMethods(unittest.TestCase):
    '''Testing the Queue module'''

    def setUp(self):
        '''Setting up'''
        self._queue = queue.Queue()

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

    def tearDown(self):
        '''Tearing down'''
        del self._queue

if __name__ == '__main__':
    unittest.main(verbosity=2)
