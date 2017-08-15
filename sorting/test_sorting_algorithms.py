'''
Testing the Hash Table module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/env python3

import unittest
from random import randint
from sorting_algorithms import bubble_sort, select_sort, insert_sort, shell_sort, merge_sort, quick_sort, heap_sort


class TestSortingMethods(unittest.TestCase):
    '''Testing the sorting algorithms'''

    def setUp(self):
        '''Setting up'''
        self._lst_to_sort = [randint(100, 999) for _ in range(100)]
        self._test_lst = self._lst_to_sort[:]
        self._test_lst.sort()

    def test_bubble_sort(self):
        '''Testing BubbleSort'''
        bubble_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_select_sort(self):
        '''Testing Selection Sort'''
        select_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_insert_sort(self):
        '''Testing Insertion Sort'''
        insert_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_shell_sort(self):
        '''Testing Shell Sort'''
        shell_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_merge_sort(self):
        '''Testing MergeSort'''
        merge_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_quick_sort(self):
        '''Testing QuickSort'''
        quick_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def test_heap_sort(self):
        '''Testing Heap Sort'''
        heap_sort(self._lst_to_sort)
        self.assertEqual(self._lst_to_sort, self._test_lst)

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
