#!/usr/bin/env python3
"""
Testing the Binary Heap module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.trees.binary_heap import BinaryHeap


class TestBinaryHeapMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.heap = BinaryHeap()
        self.heap.insert((5, "a"))
        self.heap.insert((9, "d"))
        self.heap.insert((1, "x"))
        self.heap.insert((2, "y"))
        self.heap.insert((3, "z"))

    def test_get_min(self):
        """Testing get_min method"""
        assert self.heap.get_min() == (1, "x")

    def test_insert(self):
        """Test insert() method"""
        assert len(self.heap) == 5

    def test_delete(self):
        """Test delete() method"""
        assert self.heap.delete()[1] == "x"
        assert self.heap.delete()[1] == "y"
        assert self.heap.delete()[1] == "z"
        assert self.heap.delete()[1] == "a"

    def test_is_empty(self):
        """Test is_empty() method"""
        testheap = BinaryHeap()
        assert testheap.is_empty()
        testheap.insert(42)
        assert not testheap.is_empty()

    def test_duplicates(self):
        """Test if the heap can handle duplicate values"""
        testheap = BinaryHeap()
        testheap.insert(9)
        testheap.insert(1)
        testheap.insert(8)
        testheap.insert(1)
        assert len(testheap) == 4
        assert testheap.delete() == 1
        assert testheap.delete() == 1
        assert testheap.delete() == 8

    def testheapify(self, capsys):
        """Test heapify() method"""
        testheap = BinaryHeap()
        testheap.heapify([9, 5, 6, 2, 3])
        print(testheap)
        out, err = capsys.readouterr()
        assert out.strip(), "[2, 3, 6, 5, 9]"


if __name__ == "__main__":
    pytest.main(["test_binary_heap.py"])
