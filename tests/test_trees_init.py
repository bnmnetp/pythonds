#!/usr/bin/env python3
"""
Testing the trees __init__ file
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.trees import BinaryHeap
from pythonds3.trees import BinaryTree
from pythonds3.trees import BinarySearchTree
from pythonds3.trees import AVLTree

trees = {
    "binary": BinaryTree(42),
    "binary heap": BinaryHeap(),
    "binary search": BinarySearchTree(),
    "avl": AVLTree(),
}

# Setup
@pytest.fixture(params=trees)
def set_up(request):
    return trees[request.param]


# Length of a new instance of Trees should be 0 (equivalent to empty)
# Exception is Binarary Tree -- that should be 1
def test_len(set_up):
    if isinstance(set_up, BinaryTree):
        assert len(set_up) == 1
    else:
        assert len(set_up) == 0


if __name__ == "__main__":
    pytest.main(["test_trees_init.py"])
