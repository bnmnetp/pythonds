#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005, 2010
Updated by Roman Yasinovskyy, 2017
"""


from typing import Any, Iterator, Union


class BinaryTreeNode:
    """Binary Tree Node class"""

    def __init__(
        self,
        key: Any,
        value: Any,
        left: Union["BinaryTreeNode", None] = None,
        right: Union["BinaryTreeNode", None] = None,
        parent: Union["BinaryTreeNode", None] = None,
    ) -> None:
        """Create new Tree Node"""
        self._key = key
        self._value = value
        self._left_child = left
        self._right_child = right
        self._parent = parent

    def get_left_child(self) -> Union["BinaryTreeNode", None]:
        """Return the node's left child"""
        return self._left_child

    def set_left_child(self, node) -> None:
        """Assign the node's left child"""
        self._left_child = node

    left_child = property(get_left_child, set_left_child)

    def get_right_child(self) -> Union["BinaryTreeNode", None]:
        """Return the node's right child"""
        return self._right_child

    def set_right_child(self, node) -> None:
        """Assign the node's right child"""
        self._right_child = node

    right_child = property(get_right_child, set_right_child)

    def get_parent(self) -> Union["BinaryTreeNode", None]:
        """Return the node's parent"""
        return self._parent

    def set_parent(self, node) -> None:
        """Assign the node's parent"""
        self._parent = node

    parent = property(get_parent, set_parent)

    def is_left_child(self) -> bool:
        """Check if the node is a left child"""
        return self._parent is not None and self._parent.left_child == self

    def is_right_child(self) -> bool:
        """Check if the node is a right child"""
        return self._parent is not None and self._parent.right_child == self

    def is_root(self) -> bool:
        """Check if the node is a tree root"""
        return not self._parent

    def is_leaf(self) -> bool:
        """Check if the node is a leaf"""
        return not (self._right_child or self._left_child)

    def has_a_child(self) -> bool:
        """Check if the node has any child"""
        return self._right_child is not None or self._left_child is not None

    def has_children(self) -> bool:
        """Check if the node has both children"""
        return self._right_child is not None and self._left_child is not None

    def get_key(self) -> Any:
        """Get node key"""
        return self._key

    def set_key(self, key) -> None:
        """Set node key"""
        self._key = key

    key = property(get_key, set_key)

    def get_value(self) -> Any:
        """Get node value"""
        return self._value

    def set_value(self, value) -> None:
        """Set node value"""
        self._value = value

    value = property(get_value, set_value)

    def replace_value(
        self,
        key: Any,
        value: Any,
        left: "BinaryTreeNode",
        right: "BinaryTreeNode",
    ) -> None:
        """Change node value"""
        self._key = key
        self._value = value
        self._left_child = left
        self._right_child = right
        if self.left_child:
            self._left_child.parent = self
        if self.right_child:
            self._right_child.parent = self

    def find_successor(self) -> Union["BinaryTreeNode", None]:
        """Find the node's successor"""
        successor = None
        if self._right_child:
            successor = self._right_child.find_min()
        else:
            if self._parent:
                if self.is_left_child():
                    successor = self._parent
                else:
                    self._parent.right_child = None
                    successor = self._parent.find_successor()
                    self._parent.right_child = self
        return successor

    def find_min(self) -> "BinaryTreeNode":
        """Find the smallest node in the right subtree"""
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self) -> None:
        """Splice out"""
        if self.is_leaf():
            if self.is_left_child():
                self._parent.left_child = None
            else:
                self._parent.right_child = None
        elif self.has_a_child():
            if self.left_child:
                if self.is_left_child():
                    self._parent.left_child = self._left_child
                else:
                    self._parent.right_child = self._left_child
                self._left_child.parent = self._parent
            else:
                if self.is_left_child():
                    self._parent.left_child = self._right_child
                else:
                    self._parent.right_child = self._right_child
                self._right_child.parent = self._parent

    def __iter__(self) -> Iterator:
        """The standard inorder traversal of a binary tree"""
        if self:
            if self._left_child:
                for elem in self._left_child:
                    yield elem
            yield self._key
            if self._right_child:
                for elem in self._right_child:
                    yield elem


class BinarySearchTree:
    """Binary search tree implementation"""

    def __init__(self) -> None:
        self._root: Union["BinaryTreeNode", None] = None
        self._size = 0

    def __len__(self) -> int:
        """Tree size"""
        return self._size

    def size(self) -> int:
        """Tree size"""
        return self._size

    def __iter__(self) -> Iterator:
        """Iterator"""
        return self._root.__iter__()

    def __getitem__(self, key: Any) -> Any:
        """[] getter operator override"""
        result = self.get(key)
        if result:
            return result
        raise KeyError("Error, key not in tree")

    def get_root(self) -> Union["BinaryTreeNode", None]:
        """Get tree root"""
        return self._root

    def set_root(self, node: "BinaryTreeNode") -> None:
        """Set tree root"""
        self._root = node

    root = property(get_root, set_root)

    def get(self, key: Any) -> Union[Any, None]:
        """Retrieve a value by the key"""
        if self._root:
            result = self._get(key, self._root)
            if result:
                return result.value
        return None

    def _get(
        self, key: Any, current_node: "BinaryTreeNode"
    ) -> Union["BinaryTreeNode", None]:
        """Retrieve a value by the key (helper function)"""
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __setitem__(self, key: Any, value: Any) -> None:
        """[] setter operator override"""
        self.put(key, value)

    def put(self, key: Any, value: Any) -> None:
        """Add new node"""
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = BinaryTreeNode(key, value)
        self._size = self._size + 1

    def _put(self, key: Any, value: Any, current_node: "BinaryTreeNode") -> None:
        """Add new node (helper function)"""
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = BinaryTreeNode(
                    key, value, parent=current_node
                )
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = BinaryTreeNode(
                    key, value, parent=current_node
                )

    def __contains__(self, key: Any) -> bool:
        """in operator override"""
        return bool(self._get(key, self._root))

    def __delitem__(self, key: Any) -> None:
        """del operator override"""
        self.delete(key)

    def delete(self, key) -> None:
        """Remove a node by its key"""
        if self._size > 1:
            node_to_remove = self._get(key, self._root)
            if node_to_remove:
                self._delete(node_to_remove)
                self._size = self._size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self._size == 1 and self._root.key == key:
            self._root = None
            self._size = self._size - 1
        else:
            raise KeyError("Error, key not in tree")

    def _delete(self, current_node: "BinaryTreeNode") -> None:
        """Remove a node by its key (helper function)"""
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # removing a node with one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def inorder(self) -> None:
        """In-order tree traversal"""
        self._inorder(self._root)

    def _inorder(self, tree: "BinaryTreeNode") -> None:
        """In-order tree traversal (helper function)"""
        if tree:
            self._inorder(tree.left_child)
            print(tree.key, end=" ")
            self._inorder(tree.right_child)

    def postorder(self) -> None:
        """Post-order tree traversal"""
        self._postorder(self._root)

    def _postorder(self, tree: "BinaryTreeNode") -> None:
        """Post-order tree traversal (helper function)"""
        if tree:
            self._postorder(tree.left_child)
            self._postorder(tree.right_child)
            print(tree.key, end=" ")

    def preorder(self) -> None:
        """Pre-order tree traversal"""
        self._preorder(self._root)

    def _preorder(self, tree: "BinaryTreeNode") -> None:
        """Pre-order tree traversal (helper function)"""
        if tree:
            print(tree.key, end=" ")
            self._preorder(tree.left_child)
            self._preorder(tree.right_child)

    def clear(self) -> None:
        """Remove all nodes"""
        while self._root:
            self.delete(self._root.key)
