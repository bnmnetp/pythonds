#!/usr/bin/env python3
"""
Testing the Priority Queue module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.trees.priority_queue import PriorityQueue


class TestPriorityQueueMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.priority_queue = PriorityQueue()
        self.priority_queue.insert((2, "x"))
        self.priority_queue.insert((3, "y"))
        self.priority_queue.insert((5, "z"))
        self.priority_queue.insert((6, "a"))
        self.priority_queue.insert((4, "d"))

    def test_delete(self):
        """testing delete() method"""
        assert self.priority_queue.delete() == (2, "x")
        assert self.priority_queue.delete() == (3, "y")

    def test_change_priority(self):
        """Testing change_priority() method"""
        self.priority_queue.change_priority("d", 1)
        assert self.priority_queue.delete() == (1, "d")

    def test_contains(self):
        """Testing contains() method"""
        assert "a" in self.priority_queue
        assert "b" not in self.priority_queue


if __name__ == "__main__":
    pytest.main(["test_priority_queue.py"])
