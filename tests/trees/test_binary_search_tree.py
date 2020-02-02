#!/usr/bin/env python3
"""
Testing the Binary Search Tree module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import random
from pythonds3.trees.binary_search_tree import BinarySearchTree
from pythonds3.trees.binary_search_tree import BinaryTreeNode


class TestBinarySearchTreeMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.bst = BinarySearchTree()

    def test_getput(self):
        """Testing get() and put() methods"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        assert self.bst.get(50) == "a"
        assert self.bst.get(45) == "f"
        assert self.bst.get(85) == "d"
        assert self.bst.get(10) == "b"
        assert self.bst.root.key == 50
        assert self.bst.root.value == "a"
        assert self.bst.root.left_child.key == 10
        assert self.bst.root.right_child.key == 70
        assert self.bst.root.left_child.key == 10
        assert self.bst.root.right_child.key == 70

    def test_getput_oper(self):
        """Testing get and put operations"""
        self.bst[25] = "g"
        assert self.bst[25] == "g"

    def test_find_successor(self):
        """Testing find_successor() method"""
        x = BinarySearchTree()
        x.put(10, "a")
        x.put(15, "b")
        x.put(6, "c")
        x.put(2, "d")
        x.put(8, "e")
        x.put(9, "f")
        assert x.root.left_child.left_child.find_successor().key == 6
        assert x.root.left_child.right_child.find_successor().key == 9
        assert x.root.left_child.right_child.right_child.find_successor().key == 10

    def test_len(self):
        """Testing __len__() and size() methods"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        assert self.bst.size() == 7
        assert len(self.bst) == 7

    def test_preorder(self, capsys):
        """Testing preorder traversal"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        self.bst.put(5, "g")

        self.bst.preorder()
        out, err = capsys.readouterr()
        assert out.strip() == "50 10 5 30 15 45 70 85"

    def test_inorder(self, capsys):
        """Testing inorder traversal"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        self.bst.put(5, "g")

        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 10 15 30 45 50 70 85"

    def test_postorder(self, capsys):
        """Testing postorder traversal"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        self.bst.put(5, "g")

        self.bst.postorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 15 45 30 10 85 70 50"

    def test_delete(self, capsys):
        """Testing delete() method"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        self.bst.put(5, "g")

        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 10 15 30 45 50 70 85"

        assert 10 in self.bst
        self.bst.delete(10)
        assert 10 not in self.bst

        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 15 30 45 50 70 85"

        assert self.bst.root.left_child.key == 15
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        assert self.bst.get(30) == "d"

        del self.bst[15]
        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 30 45 50 70 85"

        assert self.bst.root.left_child.key == 30
        assert self.bst.root.left_child.right_child.key == 45
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        self.bst.delete(70)
        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 30 45 50 85"
        assert 85 in self.bst
        assert self.bst.get(30) == "d"

        print(self.bst.root.key)
        out, err = capsys.readouterr()
        assert out.strip() == "50"
        print(self.bst.root.left_child.key)
        out, err = capsys.readouterr()
        assert out.strip(), "30"
        print(self.bst.root.left_child.left_child.key)
        out, err = capsys.readouterr()
        assert out.strip() == "5"
        print(self.bst.root.left_child.right_child.key)
        out, err = capsys.readouterr()
        assert out.strip() == "45"
        print(self.bst.root.right_child.key)
        out, err = capsys.readouterr()
        assert out.strip() == "85"
        self.bst.delete(50)
        assert self.bst.root.key == 85
        assert self.bst.root.left_child.key == 30
        assert not self.bst.root.right_child
        assert self.bst.root.left_child.left_child.key == 5
        assert self.bst.root.left_child.right_child.key == 45
        assert self.bst.root.left_child.left_child.parent == self.bst.root.left_child
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5 30 45 85"
        del self.bst[45]
        assert self.bst.root.left_child.key == 30
        del self.bst[85]
        assert self.bst.root.key == 30
        assert self.bst.root.left_child.parent.key == self.bst.root.key
        del self.bst[30]
        assert self.bst.root.key == 5
        self.bst.inorder()
        out, err = capsys.readouterr()
        assert out.strip() == "5"
        assert self.bst.root.key == 5
        self.bst.delete(5)
        assert not self.bst.root

    def test_delete_2(self):
        """Testing delete() method again"""
        self.bst.put(21, "a")
        self.bst.put(10, "b")
        self.bst.put(24, "c")
        self.bst.put(11, "d")
        self.bst.put(22, "d")
        self.bst.delete(10)
        assert self.bst.root.left_child.key == 11
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.key == 24
        self.bst.delete(24)
        assert self.bst.root.right_child.key == 22
        assert self.bst.root.right_child.parent == self.bst.root
        self.bst.delete(22)
        self.bst.delete(21)
        assert self.bst.root.key == 11
        assert not self.bst.root.left_child
        assert not self.bst.root.right_child

    def test_large_tree(self):
        """Testing a large random tree"""
        random_list = random.sample(range(1, 1_000_000), 1_000)
        for number in random_list:
            self.bst.put(number, number)
        sorted_list = sorted(random_list)
        for number in random_list:
            min_node = self.bst.root.find_min()
            if min_node:
                assert min_node.key == sorted_list[0]
            root_pos = sorted_list.index(self.bst.root.key)
            successor = self.bst.root.find_successor()
            if successor:
                assert successor.key == sorted_list[root_pos + 1]
            else:
                assert not self.bst.root.right_child
            self.bst.delete(number)
            sorted_list.remove(number)

        assert not self.bst.root

    def test_iter(self):
        """Testing iterator"""
        import random

        random_list = random.sample(range(1, 1_000_000), 100)
        for n in random_list:
            self.bst.put(n, n)
        sorted_list = sorted(random_list)

        i = 0
        for j in self.bst:
            assert j == sorted_list[i]
            i += 1

    """The following exercises all of the branches in deleting a node with one child"""

    def test_delete_case_1(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(7, 7)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(6, 6)
        self.bst.delete(7)
        assert self.bst.root.left_child.key == 5
        assert self.bst.root == self.bst.root.left_child.parent
        assert self.bst.root.left_child.left_child.key == 1
        assert self.bst.root.left_child.right_child.key == 6

    def test_delete_case_2(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(12, 12)
        self.bst.put(11, 11)
        self.bst.put(13, 13)
        self.bst.delete(15)
        assert self.bst.root.right_child.key == 12
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.right_child.left_child.key == 11
        assert self.bst.root.right_child.right_child.key == 13

    def test_delete_case_3(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(6, 6)
        self.bst.put(8, 8)
        self.bst.put(7, 7)
        self.bst.put(9, 9)
        self.bst.delete(6)
        assert self.bst.root.left_child.key == 8
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.left_child.left_child.key == 7
        assert self.bst.root.left_child.right_child.key == 9

    def test_delete_case_4(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete(15)
        assert self.bst.root.right_child.key == 20
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.right_child.right_child.key == 22
        assert self.bst.root.right_child.left_child.key == 17

    def test_delete_case_5(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete(10)
        assert self.bst.root.key == 20
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.left_child.key == 17
        assert self.bst.root.right_child.key == 22

    def test_delete_case_6(self):
        """Testing delete() method"""
        self.bst.put(10, 10)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(7, 7)
        self.bst.delete(10)
        assert self.bst.root.key == 5
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.right_child.parent == self.bst.root
        assert self.bst.root.left_child.key == 1
        assert self.bst.root.right_child.key == 7

    def test_delete_error(self):
        """Testing erreneous delete"""
        self.bst.put(10, 10)
        with pytest.raises(KeyError) as excinfo:
            self.bst.delete(5)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Error, key not in tree"
        self.bst.delete(10)
        with pytest.raises(KeyError) as excinfo:
            self.bst.delete(10)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Error, key not in tree"

    def test_clear(self):
        """Testing clear() method"""
        self.bst.put(50, "a")
        self.bst.put(10, "b")
        self.bst.put(70, "c")
        self.bst.put(30, "d")
        self.bst.put(85, "d")
        self.bst.put(15, "e")
        self.bst.put(45, "f")
        assert len(self.bst) == 7
        self.bst.clear()
        assert len(self.bst) == 0


if __name__ == "__main__":
    pytest.main(["test_binary_search_tree.py"])
