'''
Testing the Binary Search Tree module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from binary_search_tree import BinarySearchTree, BinaryTreeNode


class TestBinarySearchTreeMethods(unittest.TestCase):
    '''Testing the Binary Search Tree module'''

    def setUp(self):
        '''Setting up'''
        self.bst = BinarySearchTree()

    def test_getput(self):
        '''Testing get() and put() methods'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.assertEqual(self.bst.get(50), 'a')
        self.assertEqual(self.bst.get(45), 'f')
        self.assertEqual(self.bst.get(85), 'd')
        self.assertEqual(self.bst.get(10), 'b')
        self.assertEqual(self.bst.root.key, 50)
        self.assertEqual(self.bst.root.value, 'a')
        self.assertEqual(self.bst.root.child_left.key, 10)
        self.assertEqual(self.bst.root.child_right.key, 70)
        self.assertEqual(self.bst.root.child_left.key, 10)
        self.assertEqual(self.bst.root.child_right.key, 70)

    def test_getput_oper(self):
        '''Testing get and put operations'''
        self.bst[25] = 'g'
        self.assertEqual(self.bst[25], 'g')

    def test_find_successor(self):
        '''Testing find_successor() method'''
        x = BinarySearchTree()
        x.put(10, 'a')
        x.put(15, 'b')
        x.put(6, 'c')
        x.put(2, 'd')
        x.put(8, 'e')
        x.put(9, 'f')
        self.assertEqual(x.root.child_left.child_left.find_successor().key, 6)
        self.assertEqual(x.root.child_left.child_right.find_successor().key, 9)
        self.assertEqual(x.root.child_left.child_right.child_right.find_successor().key, 10)

    def test_len(self):
        '''Testing __len__() and length() methods'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.assertEqual(self.bst.size(), 7)
        self.assertEqual(len(self.bst), 7)

    def test_preorder(self):
        '''Testing preorder traversal'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')

        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.preorder()
        self.assertEqual(output.getvalue().strip(), '50 10 5 30 15 45 70 85')

    def test_inorder(self):
        '''Testing inorder traversal'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')

        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 10 15 30 45 50 70 85')

    def test_postorder(self):
        '''Testing postorder traversal'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')

        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.postorder()
        self.assertEqual(output.getvalue().strip(), '5 15 45 30 10 85 70 50')

    def test_delete(self):
        '''Testing delete() method'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')

        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 10 15 30 45 50 70 85')

        self.assertTrue(10 in self.bst)
        self.bst.delete(10)
        self.assertFalse(10 in self.bst)

        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 15 30 45 50 70 85')

        self.assertEqual(self.bst.root.child_left.key, 15)
        self.assertEqual(self.bst.root.child_left.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_left.child_right.parent, self.bst.root.child_left)
        self.assertEqual(self.bst.get(30), 'd')

        del self.bst[15]
        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 30 45 50 70 85')

        self.assertEqual(self.bst.root.child_left.key, 30)
        self.assertEqual(self.bst.root.child_left.child_right.key, 45)
        self.assertEqual(self.bst.root.child_left.child_right.parent, self.bst.root.child_left)
        self.bst.delete(70)
        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 30 45 50 85')
        self.assertTrue(85 in self.bst)
        self.assertEqual(self.bst.get(30), 'd')

        with patch('sys.stdout', new=StringIO()) as output:
            print(self.bst.root.key)
        self.assertEqual(output.getvalue().strip(), '50')
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.bst.root.child_left.key)
        self.assertEqual(output.getvalue().strip(), '30')
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.bst.root.child_left.child_left.key)
        self.assertEqual(output.getvalue().strip(), '5')
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.bst.root.child_left.child_right.key)
        self.assertEqual(output.getvalue().strip(), '45')
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.bst.root.child_right.key)
        self.assertEqual(output.getvalue().strip(), '85')
        self.bst.delete(50)
        self.assertEqual(self.bst.root.key, 85)
        self.assertEqual(self.bst.root.child_left.key, 30)
        self.assertFalse(self.bst.root.child_right)
        self.assertEqual(self.bst.root.child_left.child_left.key, 5)
        self.assertEqual(self.bst.root.child_left.child_right.key, 45)
        self.assertEqual(self.bst.root.child_left.child_left.parent, self.bst.root.child_left)
        self.assertEqual(self.bst.root.child_left.child_right.parent, self.bst.root.child_left)
        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5 30 45 85')
        del self.bst[45]
        self.assertEqual(self.bst.root.child_left.key, 30)
        del self.bst[85]
        self.assertEqual(self.bst.root.key, 30)
        self.assertEqual(self.bst.root.child_left.parent.key, self.bst.root.key)
        del self.bst[30]
        self.assertEqual(self.bst.root.key, 5)
        with patch('sys.stdout', new=StringIO()) as output:
            self.bst.inorder()
        self.assertEqual(output.getvalue().strip(), '5')
        self.assertEqual(self.bst.root.key, 5)
        self.bst.delete(5)
        self.assertFalse(self.bst.root)

    def test_delete_2(self):
        '''Testing delete() method again'''
        self.bst.put(21, 'a')
        self.bst.put(10, 'b')
        self.bst.put(24, 'c')
        self.bst.put(11, 'd')
        self.bst.put(22, 'd')
        self.bst.delete(10)
        self.assertEqual(self.bst.root.child_left.key, 11)
        self.assertEqual(self.bst.root.child_left.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_right.key, 24)
        self.bst.delete(24)
        self.assertEqual(self.bst.root.child_right.key, 22)
        self.assertEqual(self.bst.root.child_right.parent, self.bst.root)
        self.bst.delete(22)
        self.bst.delete(21)
        self.assertEqual(self.bst.root.key, 11)
        self.assertFalse(self.bst.root.child_left)
        self.assertFalse(self.bst.root.child_right)

    def test_large_tree(self):
        '''Testing a large random tree'''
        import random
        i = 0
        random_list = []
        while i < 10000:
            nrand = random.randrange(1, 10000000)
            if nrand not in random_list:
                random_list.append(nrand)
                i += 1
        # print(random_list)
        for number in random_list:
            self.bst.put(number, number)
        sorted_list = random_list[:]
        sorted_list.sort()
        random.shuffle(random_list)
        for number in random_list:
            min_node = self.bst.root.find_min()
            if min_node:
                self.assertEqual(min_node.key, sorted_list[0])
            root_pos = sorted_list.index(self.bst.root.key)
            successor = self.bst.root.find_successor()
            if successor:
                self.assertEqual(successor.key, sorted_list[root_pos + 1])
            else:
                self.assertFalse(self.bst.root.child_right)
            self.bst.delete(number)
            sorted_list.remove(number)

        self.assertFalse(self.bst.root)

    def test_iter(self):
        '''Testing iterator'''
        import random
        i = 0
        random_list = []
        while i < 100:
            nrand = random.randrange(1, 10000)
            if nrand not in random_list:
                random_list.append(nrand)
                i += 1
        for n in random_list:
            self.bst.put(n, n)
        sorted_list = random_list[:]
        sorted_list.sort()

        i = 0
        for j in self.bst:
            self.assertEqual(j, sorted_list[i])
            i += 1

    '''The following exercises all of the branches in deleting a node with one child'''
    def test_delete_case_1(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(7, 7)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(6, 6)
        self.bst.delete(7)
        self.assertEqual(self.bst.root.child_left.key, 5)
        self.assertEqual(self.bst.root, self.bst.root.child_left.parent)
        self.assertEqual(self.bst.root.child_left.child_left.key, 1)
        self.assertEqual(self.bst.root.child_left.child_right.key, 6)

    def test_delete_case_2(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(12, 12)
        self.bst.put(11, 11)
        self.bst.put(13, 13)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.child_right.key, 12)
        self.assertEqual(self.bst.root.child_right.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_right.child_left.key, 11)
        self.assertEqual(self.bst.root.child_right.child_right.key, 13)

    def test_delete_case_3(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(6, 6)
        self.bst.put(8, 8)
        self.bst.put(7, 7)
        self.bst.put(9, 9)
        self.bst.delete(6)
        self.assertEqual(self.bst.root.child_left.key, 8)
        self.assertEqual(self.bst.root.child_left.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_left.child_left.key, 7)
        self.assertEqual(self.bst.root.child_left.child_right.key, 9)

    def test_delete_case_4(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(15, 15)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete(15)
        self.assertEqual(self.bst.root.child_right.key, 20)
        self.assertEqual(self.bst.root.child_right.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_right.child_right.key, 22)
        self.assertEqual(self.bst.root.child_right.child_left.key, 17)

    def test_delete_case_5(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(20, 20)
        self.bst.put(17, 17)
        self.bst.put(22, 22)
        self.bst.delete(10)
        self.assertEqual(self.bst.root.key, 20)
        self.assertEqual(self.bst.root.child_left.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_right.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_left.key, 17)
        self.assertEqual(self.bst.root.child_right.key, 22)

    def test_delete_case_6(self):
        '''Testing delete() method'''
        self.bst.put(10, 10)
        self.bst.put(5, 5)
        self.bst.put(1, 1)
        self.bst.put(7, 7)
        self.bst.delete(10)
        self.assertEqual(self.bst.root.key, 5)
        self.assertEqual(self.bst.root.child_left.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_right.parent, self.bst.root)
        self.assertEqual(self.bst.root.child_left.key, 1)
        self.assertEqual(self.bst.root.child_right.key, 7)

    def test_delete_error(self):
        '''Testing erreneous delete'''
        self.bst.put(10, 10)
        with self.assertRaises(KeyError):
            self.bst.delete(5)
        self.bst.delete(10)
        with self.assertRaises(KeyError):
            self.bst.delete(10)

    def test_clear(self):
        '''Testing clear() method'''
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.assertEqual(len(self.bst), 7)
        self.bst.clear()
        self.assertEqual(len(self.bst), 0)

if __name__ == '__main__':
    unittest.main()
