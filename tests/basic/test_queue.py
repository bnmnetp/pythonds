#!/usr/bin/env python3
"""
Testing the Queue module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.basic.queue import Queue


class TestQueueMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.queue = Queue()

    def test_is_empty(self):
        """Testing is_empty() method"""
        assert self.queue.is_empty()
        self.queue.enqueue(42)
        assert not self.queue.is_empty()

    def test_size(self):
        """Testing size() method"""
        assert self.queue.size() == 0
        self.queue.enqueue(42)
        assert self.queue.size() == 1

    def test_enqueue(self):
        """Testing enqueue() method"""
        self.queue.enqueue(42)
        assert self.queue.size() == 1

    def test_dequeue(self):
        """Testing dequeue() method"""
        self.queue.enqueue(42)
        assert self.queue.dequeue() == 42
        assert self.queue.is_empty()


if __name__ == "__main__":
    pytest.main(["test_queue.py"])
