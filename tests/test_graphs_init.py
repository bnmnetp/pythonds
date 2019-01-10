#!/usr/bin/env python3
"""
Testing the graphs __init__ file
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.graphs import Graph

# Setup
@pytest.fixture()
def set_up():
    """Setting up"""
    graph = Graph()
    return graph


# Length of a new instance of Graph should be 0 (equivalent to empty)
def test_len(set_up):
    """Testing len() method"""
    assert len(set_up) == 0


if __name__ == "__main__":
    pytest.main(["test_graphs_init.py"])
