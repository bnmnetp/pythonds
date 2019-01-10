#!/usr/bin/env python3
"""
Testing the Deque module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.basic.deque import Deque


class TestDequeMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.deque = Deque()

    def test_is_empty(self):
        """Testing is_empty() method"""
        assert self.deque.is_empty()
        self.deque.add_front(42)
        assert not self.deque.is_empty()

    def test_size(self):
        """Testing size() method"""
        assert self.deque.size() == 0
        self.deque.add_front(42)
        assert self.deque.size() == 1

    def test_add_front(self):
        """Testing add_front() method"""
        self.deque.add_front(42)
        assert self.deque.size() == 1

    def test_add_rear(self):
        """Testing add_rear() method"""
        self.deque.add_rear(42)
        assert self.deque.size() == 1

    def test_remove_front(self):
        """Testing remove_front() method"""
        self.deque.add_front(42)
        assert self.deque.remove_front() == 42
        assert self.deque.is_empty()

    def test_remove_rear(self):
        """Testing remove_rear() method"""
        self.deque.add_rear(42)
        assert self.deque.remove_rear() == 42
        assert self.deque.is_empty()


if __name__ == "__main__":
    pytest.main(["test_deque.py"])
