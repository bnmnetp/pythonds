'''
Testing the BinaryTree module
Roman Yasinovskyy, 2017
See https://stackoverflow.com/a/31281467 for testing output
'''

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from binary_heap import BinaryHeap


class TestBinaryHeapMethods(unittest.TestCase):
    '''Testing the Binary Heap module'''

    def setUp(self):
        '''Setting up'''
        self.__heap = BinaryHeap()
        self.__heap.insert((5, 'a'))
        self.__heap.insert((9, 'd'))
        self.__heap.insert((1, 'x'))
        self.__heap.insert((2, 'y'))
        self.__heap.insert((3, 'z'))

    def test_insert(self):
        '''Test insert() method'''
        self.assertEqual(len(self.__heap), 5)

    def test_delete(self):
        '''Test delete() method'''
        self.assertEqual(self.__heap.delete()[1], 'x')
        self.assertEqual(self.__heap.delete()[1], 'y')
        self.assertEqual(self.__heap.delete()[1], 'z')
        self.assertEqual(self.__heap.delete()[1], 'a')

    def test_is_empty(self):
        '''Test is_empty() method'''
        test_heap = BinaryHeap()
        self.assertTrue(test_heap.is_empty())
        test_heap.insert(42)
        self.assertFalse(test_heap.is_empty())

    def test_duplicates(self):
        '''Test if the heap can handle duplicate values'''
        test_heap = BinaryHeap()
        test_heap.insert(9)
        test_heap.insert(1)
        test_heap.insert(8)
        test_heap.insert(1)
        self.assertEqual(len(test_heap), 4)
        self.assertEqual(test_heap.delete(), 1)
        self.assertEqual(test_heap.delete(), 1)
        self.assertEqual(test_heap.delete(), 8)

    def test_heapify(self):
        '''Test heapify() method'''
        test_heap = BinaryHeap()
        test_heap.heapify([9, 5, 6, 2, 3])
        with patch('sys.stdout', new=StringIO()) as output:
            print(test_heap)
        self.assertEqual(output.getvalue().strip(), '[2, 3, 6, 5, 9]')

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
