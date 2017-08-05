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
        self.__queue = queue.Queue()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self.__queue.is_empty())
        self.__queue.enqueue(42)
        self.assertFalse(self.__queue.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self.__queue.size(), 0)
        self.__queue.enqueue(42)
        self.assertEqual(self.__queue.size(), 1)

    def test_enqueue(self):
        '''Testing enqueue() method'''
        self.__queue.enqueue(42)
        self.assertEqual(self.__queue.size(), 1)

    def test_dequeue(self):
        '''Testing dequeue() method'''
        self.__queue.enqueue(42)
        self.assertEqual(self.__queue.dequeue(), 42)
        self.assertTrue(self.__queue.is_empty())

    def tearDown(self):
        '''Tearing down'''
        del self.__queue

if __name__ == '__main__':
    unittest.main()
