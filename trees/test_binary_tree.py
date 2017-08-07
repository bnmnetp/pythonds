'''
Testing the BinaryTree module
Roman Yasinovskyy, 2017
See https://stackoverflow.com/a/31281467 for testing output
'''

#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
from binary_tree import BinaryTree


class TestBinaryTreeMethods(unittest.TestCase):
    '''Testing the Binary Tree module'''

    def setUp(self):
        '''Setting up'''
        pass

    def test_get_root_val(self):
        '''Testing get_root_val() method'''
        self.__tree = BinaryTree('A')
        self.assertEqual(self.__tree.get_root_val(), 'A')

    def test_is_leaf(self):
        '''Testing is_leaf() method'''
        self.__tree = BinaryTree('A')
        self.assertTrue(self.__tree.is_leaf())

    def test_insert_left(self):
        '''Testing insert_left() method'''
        self.__tree = BinaryTree('A')
        self.assertEqual(self.__tree.height(), 0)
        self.__tree.insert_left('B')
        self.assertEqual(self.__tree.height(), 1)

    def test_insert_right(self):
        '''Testing insert_right() method'''
        self.__tree = BinaryTree('A')
        self.assertEqual(self.__tree.height(), 0)
        self.__tree.insert_right('C')
        self.assertEqual(self.__tree.height(), 1)

    def test_get_child_left(self):
        '''Testing get_child_left() method'''
        self.__tree = BinaryTree('A')
        self.__tree.insert_left('B')
        self.assertEqual(self.__tree.get_child_left().get_root_val(), 'B')

    def test_get_child_right(self):
        '''Testing get_child_right() method'''
        self.__tree = BinaryTree('A')
        self.__tree.insert_right('C')
        self.assertEqual(self.__tree.get_child_right().get_root_val(), 'C')

    def test_height(self):
        '''Testing height() method'''
        self.__tree = BinaryTree('A')
        self.assertEqual(self.__tree.height(), 0)
        self.__tree.insert_left('B')
        self.assertEqual(self.__tree.height(), 1)
        self.__tree.insert_right('C')
        self.assertEqual(self.__tree.height(), 1)
        self.__tree.get_child_left().insert_left('D')
        self.assertEqual(self.__tree.height(), 2)

    def test_count_nodes(self):
        '''Testing count_nodes() method'''
        self.__tree = BinaryTree('A')
        self.assertEqual(self.__tree.count_nodes(), 1)
        self.__tree.insert_left('B')
        self.assertEqual(self.__tree.count_nodes(), 2)
        self.__tree.insert_right('C')
        self.assertEqual(self.__tree.count_nodes(), 3)
        self.__tree.get_child_left().insert_left('D')
        self.assertEqual(self.__tree.count_nodes(), 4)

    def test_preorder(self):
        '''Testing preorder() method'''
        self.__tree = BinaryTree('A')
        self.__tree.insert_left('B')
        self.__tree.insert_right('C')
        self.__tree.get_child_left().insert_left('D')
        self.__tree.get_child_left().insert_right('E')
        self.__tree.get_child_right().insert_left('F')
        self.__tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self.__tree.preorder()
        self.assertEqual(output.getvalue().strip(), 'A B D E C F G')

    def test_inorder(self):
        '''Testing inorder() method'''
        self.__tree = BinaryTree('A')
        self.__tree.insert_left('B')
        self.__tree.insert_right('C')
        self.__tree.get_child_left().insert_left('D')
        self.__tree.get_child_left().insert_right('E')
        self.__tree.get_child_right().insert_left('F')
        self.__tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self.__tree.inorder()
        self.assertEqual(output.getvalue().strip(), 'D B E A F C G')

    def test_postorder(self):
        '''Testing postorder() method'''
        self.__tree = BinaryTree('A')
        self.__tree.insert_left('B')
        self.__tree.insert_right('C')
        self.__tree.get_child_left().insert_left('D')
        self.__tree.get_child_left().insert_right('E')
        self.__tree.get_child_right().insert_left('F')
        self.__tree.get_child_right().insert_right('G')

        with patch('sys.stdout', new=StringIO()) as output:
            self.__tree.postorder()
        self.assertEqual(output.getvalue().strip(), 'D E B F G C A')

    def test_print_exp(self):
        '''Testing print_exp() method'''
        self.__tree = BinaryTree('*')
        self.__tree.insert_left('+')
        left_subtree = self.__tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self.__tree.insert_right(7)

        with patch('sys.stdout', new=StringIO()) as output:
            self.__tree.print_exp()
        self.assertEqual(output.getvalue().strip(), '( ( 1 + 5 ) * 7 )')

    def test_postorder_eval(self):
        '''Testing postorder_eval() method'''
        self.__tree = BinaryTree('*')
        self.__tree.insert_left('+')
        left_subtree = self.__tree.get_child_left()
        left_subtree.insert_left(1)
        left_subtree.insert_right(5)
        self.__tree.insert_right(7)

        self.assertEqual(self.__tree.postorder_eval(), 42)

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
