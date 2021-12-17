#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

import operator
from typing import Any, Union


class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed from other trees
    rather than always creating a new tree in the insert_left or insert_right
    """

    def __init__(self, key: Any) -> None:
        """Create new tree"""
        self._key = key
        self._left_child: Union["BinaryTree", None] = None
        self._right_child: Union["BinaryTree", None] = None

    def get_root_val(self) -> Any:
        """Get root key value"""
        return self._key

    def set_root_val(self, key):
        """Set root key value"""
        self._key = key

    root = property(get_root_val, set_root_val)

    def get_left_child(self) -> Union["BinaryTree", None]:
        """Get left child"""
        return self._left_child

    def set_left_child(self, node) -> None:
        """Set left child"""
        self._left_child = node

    left_child = property(get_left_child, set_left_child)

    def get_right_child(self) -> Union["BinaryTree", None]:
        """Get right child"""
        return self._right_child

    def set_right_child(self, node) -> None:
        """Set right child"""
        self._right_child = node

    right_child = property(get_right_child, set_right_child)

    def is_leaf(self) -> bool:
        """Check if a node is leaf"""
        return (not self._left_child) and (not self._right_child)

    def insert_left(self, new_node: Any) -> None:
        """Insert left subtree"""
        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)

        if self._left_child:
            new_subtree.set_left_child(self._left_child)

        self._left_child = new_subtree

    def insert_right(self, new_node: Any) -> None:
        """Insert right subtree"""
        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)

        if self._right_child:
            new_subtree.set_right_child(self._right_child)
        self._right_child = new_subtree

    def preorder(self) -> None:
        """Pre-order tree traversal"""
        print(self._key, end=" ")
        if self._left_child:
            self._left_child.preorder()
        if self._right_child:
            self._right_child.preorder()

    def inorder(self) -> None:
        """In-order tree traversal"""
        if self._left_child:
            self._left_child.inorder()
        print(self._key, end=" ")
        if self._right_child:
            self._right_child.inorder()

    def postorder(self) -> None:
        """Post-order tree traversal"""
        if self._left_child:
            self._left_child.postorder()
        if self._right_child:
            self._right_child.postorder()
        print(self._key, end=" ")

    def print_exp(self) -> None:
        """Print an expression"""
        if self._left_child:
            print("(", end=" ")
            self._left_child.print_exp()
        print(self._key, end=" ")
        if self._right_child:
            self._right_child.print_exp()
            print(")", end=" ")

    def postorder_eval(self) -> Any:
        """Postorder evaluation"""
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        result_1 = None
        result_2 = None
        if self._left_child:
            result_1 = self._left_child.postorder_eval()
        if self._right_child:
            result_2 = self._right_child.postorder_eval()
        if result_1 and result_2:
            return operations[self._key](result_1, result_2)
        return self._key

    def height(self) -> int:
        """Height of a tree"""
        if not self._key:
            return -1
        if self._left_child:
            height_left = self._left_child.height()
        else:
            height_left = -1

        if self._right_child:
            height_right = self._right_child.height()
        else:
            height_right = -1

        return 1 + max(height_left, height_right)

    def __len__(self) -> int:
        """Size of a tree"""
        return self.size()

    def size(self) -> int:
        """Count nodes in a tree"""
        if not self._key:
            return 0
        if self._left_child:
            children_left = self._left_child.size()
        else:
            children_left = 0

        if self._right_child:
            children_right = self._right_child.size()
        else:
            children_right = 0

        return 1 + children_left + children_right
