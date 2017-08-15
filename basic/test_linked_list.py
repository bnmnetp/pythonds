'''
Testing the Linked List module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/env python3

import random
import unittest
from unittest.mock import patch
from io import StringIO
from linked_list import LinkedListNode, LinkedList, UnorderedList, OrderedList


class TestLinkedListMethods(unittest.TestCase):
    '''Testing the Linked List module'''

    def setUp(self):
        '''Setting up'''
        self._node = LinkedListNode(42)
        self._list_ordered = OrderedList()
        self._list_unordered = UnorderedList()

    def test_node_init(self):
        '''Testing node __init__ method'''
        self.assertEqual(self._node.data, 42)

    def test_node_str(self):
        '''Testing node __str__ method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self._node)
        self.assertEqual(output.getvalue().strip(), '42')

    def test_linked_list_fail(self):
        '''Testing abstract linked list class'''
        with self.assertRaises(TypeError):
            LinkedList()

    def test_ordered_list_add(self):
        '''Testing unordered list add method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_ordered.add(item)
            test_lst.insert(0, item)
        self.assertEqual(str(self._list_ordered), str(sorted(test_lst)))

    @unittest.expectedFailure  # Remove this decorator once __remove_ is implemented
    def test_ordered_list_remove(self):
        '''Testing ordered list remove method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_ordered.add(item)
            test_lst.insert(0, item)
        self.assertEqual(str(self._list_ordered), str(sorted(test_lst)))
        self._list_ordered.remove(test_lst[0])
        test_lst.remove(test_lst[0])
        self.assertEqual(str(self._list_ordered), str(sorted(test_lst)))
        self._list_ordered.remove(test_lst[5])
        test_lst.remove(test_lst[5])
        self.assertEqual(str(self._list_ordered), str(sorted(test_lst)))
        self._list_ordered.remove(test_lst[-1])
        test_lst.remove(test_lst[-1])
        self.assertEqual(str(self._list_ordered), str(sorted(test_lst)))

    @unittest.expectedFailure  # Remove this decorator once __remove__ is implemented
    def test_unordered_list_remove_err(self):
        '''Testing ordered list remove method exception'''
        for _ in range(10):
            self._list_ordered.add(random.randint(1, 10))
        with self.assertRaises(ValueError):
            self._list_ordered.remove(42)

    @unittest.expectedFailure  # Remove this decorator once __search__ is implemented
    def test_ordered_list_search(self):
        '''Testing ordered list search method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_ordered.add(item)
            test_lst.insert(0, item)
        self.assertTrue(self._list_ordered.search(test_lst[0]))
        self.assertTrue(self._list_ordered.search(test_lst[5]))
        self.assertTrue(self._list_ordered.search(test_lst[-1]))
        self.assertFalse(self._list_ordered.search(42))

    def test_unordered_list_add(self):
        '''Testing unordered list add method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_unordered.add(item)
            test_lst.insert(0, item)
        self.assertEqual(str(self._list_unordered), str(test_lst))

    def test_unordered_list_remove(self):
        '''Testing unordered list remove method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_unordered.add(item)
            test_lst.insert(0, item)
        self.assertEqual(str(self._list_unordered), str(test_lst))
        self._list_unordered.remove(test_lst[0])
        test_lst.remove(test_lst[0])
        self.assertEqual(str(self._list_unordered), str(test_lst))
        self._list_unordered.remove(test_lst[5])
        test_lst.remove(test_lst[5])
        self.assertEqual(str(self._list_unordered), str(test_lst))
        self._list_unordered.remove(test_lst[-1])
        test_lst.remove(test_lst[-1])
        self.assertEqual(str(self._list_unordered), str(test_lst))

    def test_unordered_list_remove_err(self):
        '''Testing unordered list remove method exception'''
        for _ in range(10):
            self._list_unordered.add(random.randint(1, 10))
        with self.assertRaises(ValueError):
            self._list_unordered.remove(42)

    def test_unordered_list_search(self):
        '''Testing unordered list search method'''
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self._list_unordered.add(item)
            test_lst.insert(0, item)
        self.assertTrue(self._list_unordered.search(test_lst[0]))
        self.assertTrue(self._list_unordered.search(test_lst[5]))
        self.assertTrue(self._list_unordered.search(test_lst[-1]))
        self.assertFalse(self._list_unordered.search(42))

    def test_linked_list_str(self):
        '''Testing unordered list __str__ method'''
        self._list_unordered.add(42)
        self._list_unordered.add('hello')
        with patch('sys.stdout', new=StringIO()) as output:
            print(self._list_unordered)
        self.assertEqual(output.getvalue().strip(), '[hello, 42]')

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
