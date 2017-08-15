'''
Testing the Hash Table module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/env python3

import random
import unittest
from hash_table import HashTable


class TestHashMapMethods(unittest.TestCase):
    '''Testing the Hash Table module'''

    def setUp(self):
        '''Setting up'''
        self._hash_table = HashTable()

    def test_hashmap_is_empty(self):
        '''Testing hash map is_empty() method'''
        self.assertTrue(self._hash_table.is_empty())

    def test_hashmap_size(self):
        '''Testing hash map size() method'''
        self.assertEqual(self._hash_table.size(), 0)
        self.assertEqual(len(self._hash_table), 0)

    def test_hashmap_contains(self):
        '''Testing hash map __contains__() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self._hash_table[item[0]] = item[1]
        self.assertTrue(55 in self._hash_table)
        self.assertFalse(56 in self._hash_table)

    def test_hashmap_put(self):
        '''Testing hash map put() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self._hash_table[item[0]] = item[1]
        self.assertEqual(self._hash_table.size(), 9)

    def test_hashmap_put_error(self):
        '''Testing hash map put() method exception'''
        with self.assertRaises(Exception):
            for key in range(42):
                self._hash_table[key] = random.random()

    def test_hashmap_get(self):
        '''Testing hash map get() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self._hash_table[item[0]] = item[1]
        self.assertEqual(self._hash_table[44], 'goat')
        self.assertEqual(self._hash_table[55], 'pig')

    def test_hashmap_get_error(self):
        '''Testing hash map get() method exception'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self._hash_table[item[0]] = item[1]
        self.assertRaises(KeyError, self._hash_table.get, *[1])

    def tearDown(self):
        '''Tearing down'''
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
