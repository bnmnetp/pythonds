'''
Testing the Deque module
Roman Yasinovskyy, 2017
'''

import unittest
import deque


class TestDequeMethods(unittest.TestCase):
    '''Testing the Deque module'''

    def setUp(self):
        '''Setting up'''
        self.__deque = deque.Deque()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self.__deque.is_empty())
        self.__deque.add_front(42)
        self.assertFalse(self.__deque.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self.__deque.size(), 0)
        self.__deque.add_front(42)
        self.assertEqual(self.__deque.size(), 1)

    def test_add_front(self):
        '''Testing add_front() method'''
        self.__deque.add_front(42)
        self.assertEqual(self.__deque.size(), 1)

    def test_add_rear(self):
        '''Testing add_rear() method'''
        self.__deque.add_rear(42)
        self.assertEqual(self.__deque.size(), 1)

    def test_remove_front(self):
        '''Testing remove_front() method'''
        self.__deque.add_front(42)
        self.assertEqual(self.__deque.remove_front(), 42)
        self.assertTrue(self.__deque.is_empty())

    def test_remove_rear(self):
        '''Testing remove_rear() method'''
        self.__deque.add_rear(42)
        self.assertEqual(self.__deque.remove_rear(), 42)
        self.assertTrue(self.__deque.is_empty())

    def tearDown(self):
        '''Tearing down'''
        del self.__deque

if __name__ == '__main__':
    unittest.main()
