'''
Testing the Binary Tree module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from pythonds3.trees.avl_tree import AVLTree


class TestBinarySearchTreeMethods(unittest.TestCase):
    '''Testing the Binary Tree module'''
    def setUp(self):
        '''Setting up'''
        self._avl_tree = AVLTree()

    def test_init(self):
        '''Testing __init__() method'''
        self.assertIsNone(self._avl_tree.root)
        self._avl_tree.put(30, 'a')
        self.assertIsNotNone(self._avl_tree.root)

    def test_len(self):
        '''Testing __len__() method'''
        self.assertEqual(self._avl_tree.size(), 0)
        self._avl_tree.put(30, 'a')
        self.assertEqual(len(self._avl_tree), 1)

    def test_auto_1(self):
        '''Testing case 1'''
        self._avl_tree.put(30, 'a')
        self._avl_tree.put(50, 'b')
        self._avl_tree.put(40, 'c')
        self.assertEqual(self._avl_tree.root.key, 40)

    def test_auto_2(self):
        '''Testing case 2'''
        self._avl_tree.put(50, 'a')
        self._avl_tree.put(30, 'b')
        self._avl_tree.put(40, 'c')
        self.assertEqual(self._avl_tree.root.key, 40)

    def test_auto_3(self):
        '''Testing case 3'''
        self._avl_tree.put(50, 'a')
        self._avl_tree.put(30, 'b')
        self._avl_tree.put(70, 'c')
        self._avl_tree.put(80, 'c')
        self._avl_tree.put(60, 'd')
        self._avl_tree.put(90, 'e')
        self.assertEqual(self._avl_tree.root.key, 70)

    def test_auto_4(self):
        '''Testing case 4'''
        self._avl_tree.put(40, 'a')
        self._avl_tree.put(30, 'b')
        self._avl_tree.put(50, 'c')
        self._avl_tree.put(45, 'd')
        self._avl_tree.put(60, 'e')
        self._avl_tree.put(43, 'f')
        self.assertEqual(self._avl_tree.root.key, 45)
        self.assertEqual(self._avl_tree.root.child_left.key, 40)
        self.assertEqual(self._avl_tree.root.child_right.key, 50)
        self.assertEqual(self._avl_tree.root.balance_factor, 0)
        self.assertEqual(self._avl_tree.root.child_left.balance_factor, 0)
        self.assertEqual(self._avl_tree.root.child_right.balance_factor, -1)

    def test_auto_5(self):
        '''Testing case 5'''
        self._avl_tree.put(40, 'a')
        self._avl_tree.put(30, 'b')
        self._avl_tree.put(50, 'c')
        self._avl_tree.put(10, 'd')
        self._avl_tree.put(35, 'e')
        self._avl_tree.put(37, 'f')
        self.assertEqual(self._avl_tree.root.key, 35)
        self.assertEqual(self._avl_tree.root.child_left.key, 30)
        self.assertEqual(self._avl_tree.root.child_right.key, 40)
        self.assertEqual(self._avl_tree.root.balance_factor, 0)
        self.assertEqual(self._avl_tree.root.child_left.balance_factor, 1)
        self.assertEqual(self._avl_tree.root.child_right.balance_factor, 0)

if __name__ == '__main__':
    unittest.main()
