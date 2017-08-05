'''
Testing the Stack module
Roman Yasinovskyy, 2017
'''

import unittest
import stack


class TestStackMethods(unittest.TestCase):
    '''Testing the Stack module'''

    def setUp(self):
        '''Setting up'''
        self.__stack = stack.Stack()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self.__stack.is_empty())
        self.__stack.push(42)
        self.assertFalse(self.__stack.is_empty())

    def test_size(self):
        '''Testing size() method'''
        self.assertEqual(self.__stack.size(), 0)
        self.__stack.push(42)
        self.assertEqual(self.__stack.size(), 1)

    def test_push(self):
        '''Testing push() method'''
        self.__stack.push(42)
        self.assertEqual(self.__stack.size(), 1)

    def test_pop(self):
        '''Testing pop() method'''
        self.__stack.push(42)
        self.assertEqual(self.__stack.pop(), 42)
        self.assertTrue(self.__stack.is_empty())

    def test_peek(self):
        '''Testing peek() method'''
        self.__stack.push(42)
        self.assertEqual(self.__stack.peek(), 42)
        self.assertEqual(self.__stack.size(), 1)

    def tearDown(self):
        '''Tearing down'''
        del self.__stack

if __name__ == '__main__':
    unittest.main()
