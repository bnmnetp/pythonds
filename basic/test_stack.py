'''
Testing the Stack module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from stack import Stack


class TestStackMethods(unittest.TestCase):
    '''Testing the Stack module'''

    def setUp(self):
        '''Setting up'''
        self._stack = Stack()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self._stack.is_empty())
        self._stack.push(42)
        self.assertFalse(self._stack.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self._stack.size(), 0)
        self._stack.push(42)
        self.assertEqual(self._stack.size(), 1)

    def test_push(self):
        '''Testing push() method'''
        self._stack.push(42)
        self.assertEqual(self._stack.size(), 1)

    def test_pop(self):
        '''Testing pop() method'''
        self._stack.push(42)
        self.assertEqual(self._stack.pop(), 42)
        self.assertTrue(self._stack.is_empty())

    def test_peek(self):
        '''Testing peek() method'''
        self._stack.push(42)
        self.assertEqual(self._stack.peek(), 42)
        self.assertEqual(self._stack.size(), 1)

if __name__ == '__main__':
    unittest.main()
