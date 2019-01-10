#!/usr/bin/env python3
"""
Testing the Sorting algorithms
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from random import randint
from pythonds3.sorting.sorting_algorithms import bubble_sort
from pythonds3.sorting.sorting_algorithms import select_sort
from pythonds3.sorting.sorting_algorithms import insert_sort
from pythonds3.sorting.sorting_algorithms import shell_sort
from pythonds3.sorting.sorting_algorithms import merge_sort
from pythonds3.sorting.sorting_algorithms import quick_sort
from pythonds3.sorting.sorting_algorithms import heap_sort


class TestSortingMethods:
    """Testing the sorting algorithms"""

    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.lst_to_sort = [randint(100, 999) for _ in range(100)]
        self.test_lst = self.lst_to_sort[:]
        self.test_lst.sort()

    def test_bubble_sort(self):
        """Testing BubbleSort"""
        bubble_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_select_sort(self):
        """Testing Selection Sort"""
        select_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_insert_sort(self):
        """Testing Insertion Sort"""
        insert_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_shell_sort(self):
        """Testing Shell Sort"""
        shell_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_merge_sort(self):
        """Testing MergeSort"""
        merge_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_quick_sort(self):
        """Testing QuickSort"""
        quick_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst

    def test_heap_sort(self):
        """Testing Heap Sort"""
        heap_sort(self.lst_to_sort)
        assert self.lst_to_sort == self.test_lst


if __name__ == "__main__":
    pytest.main(["test_sorting_algorithms.py"])
