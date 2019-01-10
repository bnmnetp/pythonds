#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005, 2010
Updated by Roman Yasinovskyy, 2017
"""

from pythonds3.trees.binary_search_tree import BinarySearchTree
from pythonds3.trees.binary_search_tree import BinaryTreeNode


class AVLTreeNode(BinaryTreeNode):
    """AVL Tree Node"""

    def __init__(self, key, val, balance_factor, left=None, right=None, parent=None):
        """Create an AVL tree node"""
        BinaryTreeNode.__init__(self, key, val, left, right, parent)
        self._balance_factor = balance_factor

    def get_balance_factor(self):
        """Get the node balance factor"""
        return self._balance_factor

    def set_balance_factor(self, value):
        """Set the node balance factor"""
        self._balance_factor = value

    balance_factor = property(get_balance_factor, set_balance_factor)


class AVLTree(BinarySearchTree):
    """AVL tree implementation"""

    def __init__(self):
        """Create a new AVL tree"""
        BinarySearchTree.__init__(self)

    def put(self, key, value):
        """Add new node"""
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = AVLTreeNode(key, value, 0)
        self._size = self._size + 1

    def _put(self, key, value, current_node):
        """Add a new node to the tree (helper function)"""
        if key < current_node.key:
            if current_node.get_child_left():
                self._put(key, value, current_node.child_left)
            else:
                current_node.child_left = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.child_left)
        else:
            if current_node.get_child_right():
                self._put(key, value, current_node.child_right)
            else:
                current_node.child_right = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.child_right)

    def update_balance(self, node):
        """Update the tree balance"""
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_child_left():
                node.parent.balance_factor += 1
            elif node.is_child_right():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        """Rebalance the tree"""
        if node.balance_factor < 0:
            if node.child_right.balance_factor > 0:
                # Do an LR Rotation
                self.rotate_right(node.child_right)
                self.rotate_left(node)
            else:
                # single left
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.child_left.balance_factor < 0:
                # Do an RL Rotation
                self.rotate_left(node.child_left)
                self.rotate_right(node)
            else:
                # single right
                self.rotate_right(node)

    def rotate_left(self, rotation_root):
        """Left rotation"""
        new_root = rotation_root.child_right
        rotation_root.child_right = new_root.child_left
        if new_root.child_left:
            new_root.child_left.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_child_left():
                rotation_root.parent.child_left = new_root
            else:
                rotation_root.parent.child_right = new_root
        new_root.child_left = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)
        )

    def rotate_right(self, rotation_root):
        """Right rotation"""
        new_root = rotation_root.child_left
        rotation_root.child_left = new_root.child_right
        if new_root.child_right:
            new_root.child_right.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_child_right():
                rotation_root.parent.child_right = new_root
            else:
                rotation_root.parent.child_left = new_root
        new_root.child_right = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor - 1 + min(rotation_root.balance_factor, 0)
        )
