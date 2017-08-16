'''
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005, 2010
Updated by Roman Yasinovskyy, 2017
'''


class BinaryTreeNode:
    '''Binary Tree Node class'''
    def __init__(self, key, value, left=None, right=None, parent=None):
        '''Create new Tree Node'''
        self._key = key
        self._value = value
        self._child_left = left
        self._child_right = right
        self._parent = parent

    def get_child_left(self):
        '''Return the node's left child'''
        return self._child_left

    def set_child_left(self, node):
        '''Assign the node's left child'''
        self._child_left = node

    child_left = property(get_child_left, set_child_left)

    def get_child_right(self):
        '''Return the node's right child'''
        return self._child_right

    def set_child_right(self, node):
        '''Assign the node's right child'''
        self._child_right = node

    child_right = property(get_child_right, set_child_right)

    def get_parent(self):
        '''Return the node's parent'''
        return self._parent

    def set_parent(self, node):
        '''Assign the node's parent'''
        self._parent = node

    parent = property(get_parent, set_parent)

    def is_child_left(self):
        '''Check if the node is a left child'''
        return self._parent and self._parent.child_left == self

    def is_child_right(self):
        '''Check if the node is a right child'''
        return self._parent and self._parent.child_right == self

    def is_root(self):
        '''Check if the node is a tree root'''
        return not self._parent

    def is_leaf(self):
        '''Check if the node is a leaf'''
        return not (self._child_right or self._child_left)

    def has_a_child(self):
        '''Check if the node has any child'''
        return self._child_right or self._child_left

    def has_children(self):
        '''Check if the node has both children'''
        return self._child_right and self._child_left

    def get_key(self):
        '''Get node key'''
        return self._key

    def set_key(self, key):
        '''Set node key'''
        self._key = key

    key = property(get_key, set_key)

    def get_value(self):
        '''Get node value'''
        return self._value

    def set_value(self, value):
        '''Set node value'''
        self._value = value

    value = property(get_value, set_value)

    def replace_payload(self, key, value, left, right):
        '''Change node payload'''
        self._key = key
        self._value = value
        self._child_left = left
        self._child_right = right
        if self.child_left:
            self._child_left.parent = self
        if self.child_right:
            self._child_right.parent = self

    def find_successor(self):
        '''Find the node's successor'''
        successor = None
        if self._child_right:
            successor = self._child_right.find_min()
        else:
            if self._parent:
                if self.is_child_left():
                    successor = self._parent
                else:
                    self._parent.child_right = None
                    successor = self._parent.find_successor()
                    self._parent.child_right = self
        return successor

    def find_min(self):
        '''Find the smallest node in the right subtree'''
        current = self
        while current.child_left:
            current = current.child_left
        return current

    def splice_out(self):
        '''Splice out'''
        if self.is_leaf():
            if self.is_child_left():
                self._parent.child_left = None
            else:
                self._parent.child_right = None
        elif self.has_a_child():
            if self.child_left:
                if self.is_child_left():
                    self._parent.child_left = self._child_left
                else:
                    self._parent.child_right = self._child_left
                self._child_left.parent = self._parent
            else:
                if self.is_child_left():
                    self._parent.child_left = self._child_right
                else:
                    self._parent.child_right = self._child_right
                self._child_right.parent = self._parent

    def __iter__(self):
        '''The standard inorder traversal of a binary tree'''
        if self:
            if self._child_left:
                for elem in self._child_left:
                    yield elem
            yield self._key
            if self._child_right:
                for elem in self._child_right:
                    yield elem


class BinarySearchTree:
    '''Binary search tree implementation'''
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        '''Tree size'''
        return self._size

    def size(self):
        '''Tree size'''
        return self._size

    def __iter__(self):
        '''Iterator'''
        return self._root.__iter__()

    def __getitem__(self, key):
        '''[] getter operator override'''
        result = self.get(key)
        if result:
            return result
        else:
            raise KeyError('Error, key not in tree')

    def get_root(self):
        '''Get tree root'''
        return self._root

    def set_root(self, node):
        '''Set tree root'''
        self._root = node

    root = property(get_root, set_root)

    def get(self, key):
        '''Retrieve a value by the key'''
        if self._root:
            result = self._get(key, self._root)
            if result:
                return result.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        '''Retrieve a value by the key (helper function)'''
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.child_left)
        else:
            return self._get(key, current_node.child_right)

    def __setitem__(self, key, value):
        '''[] setter operator override'''
        self.put(key, value)

    def put(self, key, value):
        '''Add new node'''
        if self._root:
            self._put(key, value, self._root)
        else:
            self._root = BinaryTreeNode(key, value)
        self._size = self._size + 1

    def _put(self, key, value, current_node):
        '''Add new node (helper function)'''
        if key < current_node.key:
            if current_node.child_left:
                self._put(key, value, current_node.child_left)
            else:
                current_node.child_left = BinaryTreeNode(key, value, parent=current_node)
        else:
            if current_node.child_right:
                self._put(key, value, current_node.child_right)
            else:
                current_node.child_right = BinaryTreeNode(key, value, parent=current_node)

    def __contains__(self, key):
        '''in operator override'''
        return bool(self._get(key, self._root))

    def __delitem__(self, key):
        '''del operator override'''
        self.delete(key)

    def delete(self, key):
        '''Remove a node by its key'''
        if self._size > 1:
            node_to_remove = self._get(key, self._root)
            if node_to_remove:
                self._delete(node_to_remove)
                self._size = self._size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self._size == 1 and self._root.key == key:
            self._root = None
            self._size = self._size - 1
        else:
            raise KeyError('Error, key not in tree')

    def _delete(self, current_node):
        '''Remove a node by its key (helper function)'''
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.child_left:
                current_node.parent.child_left = None
            else:
                current_node.parent.child_right = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # removing a node with one child
            if current_node.get_child_left():
                if current_node.is_child_left():
                    current_node.child_left.parent = current_node.parent
                    current_node.parent.child_left = current_node.child_left
                elif current_node.is_child_right():
                    current_node.child_left.parent = current_node.parent
                    current_node.parent.child_right = current_node.child_left
                else:
                    current_node.replace_payload(current_node.child_left.key,
                                                 current_node.child_left.value,
                                                 current_node.child_left.child_left,
                                                 current_node.child_left.child_right)
            else:
                if current_node.is_child_left():
                    current_node.child_right.parent = current_node.parent
                    current_node.parent.child_left = current_node.child_right
                elif current_node.is_child_right():
                    current_node.child_right.parent = current_node.parent
                    current_node.parent.child_right = current_node.child_right
                else:
                    current_node.replace_payload(current_node.child_right.key,
                                                 current_node.child_right.value,
                                                 current_node.child_right.child_left,
                                                 current_node.child_right.child_right)

    def inorder(self):
        '''In-order tree traversal'''
        self._inorder(self._root)

    def _inorder(self, tree):
        '''In-order tree traversal (helper function)'''
        if tree:
            self._inorder(tree.child_left)
            print(tree.key, end=' ')
            self._inorder(tree.child_right)

    def postorder(self):
        '''Post-order tree traversal'''
        self._postorder(self._root)

    def _postorder(self, tree):
        '''Post-order tree traversal (helper function)'''
        if tree:
            self._postorder(tree.child_left)
            self._postorder(tree.child_right)
            print(tree.key, end=' ')

    def preorder(self):
        '''Pre-order tree traversal'''
        self._preorder(self._root)

    def _preorder(self, tree):
        '''Pre-order tree traversal (helper function)'''
        if tree:
            print(tree.key, end=' ')
            self._preorder(tree.child_left)
            self._preorder(tree.child_right)

    def clear(self):
        '''Remove all nodes'''
        while self._root:
            self.delete(self._root.key)
