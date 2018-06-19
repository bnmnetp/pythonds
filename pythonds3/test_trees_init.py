'''
Testing the trees __init__ file
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from trees import BinaryHeap, BinaryTree, BinarySearchTree, AVLTree


class TestTreesInit(unittest.TestCase):
    '''Testing the trees __init__ file'''

    def setUp(self):
        '''Setting up'''
        self._binary_tree = BinaryTree(42)
        self._binary_heap = BinaryHeap()
        self._binary_search_tree = BinarySearchTree()
        self._avl_tree = AVLTree()

    def test_len(self):
        '''Testing len() method'''
        self.assertEqual(len(self._binary_tree), 1)
        self.assertEqual(len(self._binary_heap), 0)
        self.assertEqual(len(self._binary_search_tree), 0)
        self.assertEqual(len(self._avl_tree), 0)

if __name__ == '__main__':
    unittest.main()
