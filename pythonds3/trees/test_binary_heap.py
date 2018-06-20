'''
Testing the Binary Heap module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from pythonds3.trees.binary_heap import BinaryHeap


class TestBinaryHeapMethods(unittest.TestCase):
    '''Testing the Binary Heap module'''

    def setUp(self):
        '''Setting up'''
        self._heap = BinaryHeap()
        self._heap.insert((5, 'a'))
        self._heap.insert((9, 'd'))
        self._heap.insert((1, 'x'))
        self._heap.insert((2, 'y'))
        self._heap.insert((3, 'z'))

    def test_contains(self):
        '''Testing __contains__ method'''
        self.assertTrue((5, 'a') in self._heap)
        self.assertFalse((65, 'b') in self._heap)

    def test_insert(self):
        '''Test insert() method'''
        self.assertEqual(len(self._heap), 5)

    def test_delete(self):
        '''Test delete() method'''
        self.assertEqual(self._heap.delete()[1], 'x')
        self.assertEqual(self._heap.delete()[1], 'y')
        self.assertEqual(self._heap.delete()[1], 'z')
        self.assertEqual(self._heap.delete()[1], 'a')

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

if __name__ == '__main__':
    unittest.main()
