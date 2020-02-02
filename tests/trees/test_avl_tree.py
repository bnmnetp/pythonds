#!/usr/bin/env python3
"""
Testing the Balanced Binary Search Tree module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.trees.avl_tree import AVLTree


class TestBalancedBinarySearchTreeMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.avl_tree = AVLTree()

    def test_init(self):
        """Testing __init__() method"""
        assert self.avl_tree.root == None
        self.avl_tree.put(30, "a")
        assert not self.avl_tree.root == None

    def test_len(self):
        """Testing __len__() method"""
        assert self.avl_tree.size() == 0
        self.avl_tree.put(30, "a")
        assert len(self.avl_tree) == 1

    def test_auto_1(self):
        """Testing case 1"""
        self.avl_tree.put(30, "a")
        self.avl_tree.put(50, "b")
        self.avl_tree.put(40, "c")
        assert self.avl_tree.root.key == 40

    def test_auto_2(self):
        """Testing case 2"""
        self.avl_tree.put(50, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(40, "c")
        assert self.avl_tree.root.key == 40

    def test_auto_3(self):
        """Testing case 3"""
        self.avl_tree.put(50, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(70, "c")
        self.avl_tree.put(80, "c")
        self.avl_tree.put(60, "d")
        self.avl_tree.put(90, "e")
        assert self.avl_tree.root.key == 70

    def test_auto_4(self):
        """Testing case 4"""
        self.avl_tree.put(40, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(50, "c")
        self.avl_tree.put(45, "d")
        self.avl_tree.put(60, "e")
        self.avl_tree.put(43, "f")
        assert self.avl_tree.root.key == 45
        assert self.avl_tree.root.left_child.key == 40
        assert self.avl_tree.root.right_child.key == 50
        assert self.avl_tree.root.balance_factor == 0
        assert self.avl_tree.root.left_child.balance_factor == 0
        assert self.avl_tree.root.right_child.balance_factor == -1

    def test_auto_5(self):
        """Testing case 5"""
        self.avl_tree.put(40, "a")
        self.avl_tree.put(30, "b")
        self.avl_tree.put(50, "c")
        self.avl_tree.put(10, "d")
        self.avl_tree.put(35, "e")
        self.avl_tree.put(37, "f")
        assert self.avl_tree.root.key == 35
        assert self.avl_tree.root.left_child.key == 30
        assert self.avl_tree.root.right_child.key == 40
        assert self.avl_tree.root.balance_factor == 0
        assert self.avl_tree.root.left_child.balance_factor == 1
        assert self.avl_tree.root.right_child.balance_factor == 0


if __name__ == "__main__":
    pytest.main(["test_avl_tree.py"])
