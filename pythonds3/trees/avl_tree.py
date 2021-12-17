#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005, 2010
Updated by Roman Yasinovskyy, 2017
"""

from typing import Any, Union

from pythonds3.trees.binary_search_tree import BinarySearchTree, BinaryTreeNode


class AVLTreeNode(BinaryTreeNode):
    """AVL Tree Node"""

    def __init__(
        self,
        key: Any,
        val: Any,
        balance_factor: int,
        left: Union["AVLTreeNode", None] = None,
        right: Union["AVLTreeNode", None] = None,
        parent: Union["AVLTreeNode", None] = None,
    ) -> None:
        """Create an AVL tree node"""
        BinaryTreeNode.__init__(self, key, val, left, right, parent)
        self._balance_factor = balance_factor

    def get_balance_factor(self) -> int:
        """Get the node balance factor"""
        return self._balance_factor

    def set_balance_factor(self, value: int) -> None:
        """Set the node balance factor"""
        self._balance_factor = value

    balance_factor = property(get_balance_factor, set_balance_factor)


class AVLTree(BinarySearchTree):
    """AVL tree implementation"""

    def __init__(self) -> None:
        """Create a new AVL tree"""
        BinarySearchTree.__init__(self)

    def put(self, key: Any, value: Any) -> None:
        """Add new node"""
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = AVLTreeNode(key, value, 0)
        self._size = self._size + 1

    def _put(self, key: Any, value: Any, current_node) -> None:
        """Add a new node to the tree (helper function)"""
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.left_child)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(
                    key, value, 0, parent=current_node
                )
                self.update_balance(current_node.right_child)

    def update_balance(self, node: "AVLTreeNode") -> None:
        """Update the tree balance"""
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node: "AVLTreeNode") -> None:
        """Rebalance the tree"""
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                # Do an LR Rotation
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                # single left
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                # Do an RL Rotation
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                # single right
                self.rotate_right(node)

    def rotate_left(self, rotation_root: "AVLTreeNode") -> None:
        """Left rotation"""
        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)
        )

    def rotate_right(self, rotation_root: "AVLTreeNode") -> None:
        """Right rotation"""
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self._root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
            rotation_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
            new_root.balance_factor - 1 + min(rotation_root.balance_factor, 0)
        )
