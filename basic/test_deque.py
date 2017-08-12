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
        self._deque = deque.Deque()

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

    def tearDown(self):
        '''Tearing down'''
        del self._deque

if __name__ == '__main__':
    unittest.main(verbosity=2)
