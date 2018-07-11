'''
Testing the Hash Table module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..')))

import random
import pytest

from pythonds3.searching.hash_table import HashTable


class TestHashMapMethods(unittest.TestCase):

    @pytest.fixture(scope = 'function', autouse = true)
    def setup_class(cls):
        '''Setting up'''
        cls.hash_table = HashTable()

    def test_hashmap_is_empty(self):
        '''Testing hash map is_empty() method'''
        assert self.hash_table.is_empty()

    def test_hashmap_size(self):
        '''Testing hash map size() method'''
        assert self.hash_table.size() == 0
        assert len(self._hash_table) == 0

    def test_hashmap_contains(self):
        '''Testing hash map __contains__() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert 55 in self._hash_table
        assert 56 in self._hash_table

    def test_hashmap_put(self):
        '''Testing hash map put() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert self.hash_table.size() == 9

    def test_hashmap_put_error(self):
        '''Testing hash map put() method exception'''
        with pytest.raises(Exception):#as excinfo:
            for key in range(42):
                self.hash_table[key] = random.random()
        

    def test_hashmap_get(self):
        '''Testing hash map get() method'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert self.hash_table[44] == 'goat'
        assert self.hash_table[55] == 'pig'

    def test_hashmap_get_error(self):
        '''Testing hash map get() method exception'''
        items = [(54, 'cat'), (26, 'dog'), (93, 'lion'), (17, 'tiger'), (77, 'bird'),
                 (31, 'cow'), (44, 'goat'), (55, 'pig'), (20, 'chicken')]
        for item in items:
            self.hash_table[item[0]] = item[1]
        with pytest.raises(KeyError):
            self.hash_table.get(*[1]) #huh
        #self.assertRaises(KeyError, self._hash_table.get, *[1])

if __name__ == '__main__':
    unittest.main()
