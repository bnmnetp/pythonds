'''
Testing the Binary Tree module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from binary_tree import BinaryTree


class TestBinaryTreeMethods(unittest.TestCase):
    '''Testing the Binary Tree module'''

    def setUp(self):
        '''Setting up'''
        self._tree = BinaryTree('A')

    def test_get_root_val(self):
        '''Testing get_root_val() method'''
        self.assertEqual(self._tree.get_root_val(), 'A')

    def test_is_leaf(self):
        '''Testing is_leaf() method'''
        self.assertTrue(self._tree.is_leaf())

    def test_insert_left(self):
        '''Testing insert_left() method'''
        self.assertEqual(self._tree.height(), 0)
        self._tree.insert_left('B')
        self.assertEqual(self._tree.height(), 1)

    def test_insert_right(self):
        '''Testing insert_right() method'''
        self.assertEqual(self._tree.height(), 0)
        self._tree.insert_right('C')
        self.assertEqual(self._tree.height(), 1)

    def test_get_child_left(self):
        '''Testing get_child_left() method'''
        self._tree.insert_left('B')
        self.assertEqual(self._tree.get_child_left().get_root_val(), 'B')

    def test_get_child_right(self):
        '''Testing get_child_right() method'''
        self._tree.insert_right('C')
        self.assertEqual(self._tree.get_child_right().get_root_val(), 'C')

    def test_height(self):
        '''Testing height() method'''
        self.assertEqual(self._tree.height(), 0)
        self._tree.insert_left('B')
        self.assertEqual(self._tree.height(), 1)
        self._tree.insert_right('C')
        self.assertEqual(self._tree.height(), 1)
        self._tree.get_child_left().insert_left('D')
        self.assertEqual(self._tree.height(), 2)

    def test_size(self):
        '''Testing count_nodes() method'''
        self.assertEqual(self._tree.size(), 1)
        self.assertEqual(len(self._tree), 1)
        self._tree.insert_left('B')
        self.assertEqual(self._tree.size(), 2)
        self._tree.insert_right('C')
        self.assertEqual(self._tree.size(), 3)
        self._tree.get_child_left().insert_left('D')
        self.assertEqual(self._tree.size(), 4)
        self.assertEqual(len(self._tree), 4)

    def test_preorder(self):
        '''Testing preorder() method'''
        self._tree.insert_left('B')
        self._tree.insert_right('C')
        self._tree.get_child_left().insert_left('D')
        self._tree.get_child_left().insert_right('E')
        self._tree.get_child_right().insert_left('F')
        self._tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self._tree.preorder()
        self.assertEqual(output.getvalue().strip(), 'A B D E C F G')

    def test_inorder(self):
        '''Testing inorder() method'''
        self._tree.insert_left('B')
        self._tree.insert_right('C')
        self._tree.get_child_left().insert_left('D')
        self._tree.get_child_left().insert_right('E')
        self._tree.get_child_right().insert_left('F')
        self._tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self._tree.inorder()
        self.assertEqual(output.getvalue().strip(), 'D B E A F C G')

    def test_postorder(self):
        '''Testing postorder() method'''
        self._tree.insert_left('B')
        self._tree.insert_right('C')
        self._tree.get_child_left().insert_left('D')
        self._tree.get_child_left().insert_right('E')
        self._tree.get_child_right().insert_left('F')
        self._tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self._tree.postorder()
        self.assertEqual(output.getvalue().strip(), 'D E B F G C A')

    def test_print_exp(self):
        '''Testing print_exp() method'''
        self._tree = BinaryTree('*')
        self._tree.insert_left('+')
        left_subtree = self._tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self._tree.insert_right(7)

        with patch('sys.stdout', new=StringIO()) as output:
            self._tree.print_exp()
        self.assertEqual(output.getvalue().strip(), '( ( 1 + 5 ) * 7 )')

    def test_postorder_eval(self):
        '''Testing postorder_eval() method'''
        self._tree = BinaryTree('*')
        self._tree.insert_left('+')
        left_subtree = self._tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self._tree.insert_right(7)

        self.assertEqual(self._tree.postorder_eval(), 42)

if __name__ == '__main__':
    unittest.main()
