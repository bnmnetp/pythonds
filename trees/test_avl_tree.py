'''
Testing the BinaryTree module
Roman Yasinovskyy, 2017
See https://stackoverflow.com/a/31281467 for testing output
'''

#!/usr/bin/env python3

import unittest
from avl_tree import AVLTree


class TestBinarySearchTreeMethods(unittest.TestCase):
    '''Testing the Binary Tree module'''
    def setUp(self):
        '''Setting up'''
        self.bst = AVLTree()

    def test_auto_1(self):
        '''Testing case 1'''
        self.bst.put(30, 'a')
        self.bst.put(50, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def test_auto_2(self):
        '''Testing case 2'''
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(40, 'c')
        assert self.bst.root.key == 40

    def test_auto_3(self):
        '''Testing case 3'''
        self.bst.put(50, 'a')
        self.bst.put(30, 'b')
        self.bst.put(70, 'c')
        self.bst.put(80, 'c')
        self.bst.put(60, 'd')
        self.bst.put(90, 'e')
        assert self.bst.root.key == 70

    def test_auto_4(self):
        '''Testing case 4'''
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(45, 'd')
        self.bst.put(60, 'e')
        self.bst.put(43, 'f')
        assert self.bst.root.key == 45
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.leftChild.balance_factor == 0
        assert self.bst.root.rightChild.balance_factor == -1

    def test_auto_5(self):
        '''Testing case 5'''
        self.bst.put(40, 'a')
        self.bst.put(30, 'b')
        self.bst.put(50, 'c')
        self.bst.put(10, 'd')
        self.bst.put(35, 'e')
        self.bst.put(37, 'f')
        assert self.bst.root.key == 35
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild.key == 40
        assert self.bst.root.balance_factor == 0
        assert self.bst.root.leftChild.balance_factor == 1
        assert self.bst.root.rightChild.balance_factor == 0

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
