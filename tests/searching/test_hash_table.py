#!/usr/bin/env python3
"""
Testing the Hash Table module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import random

from pythonds3.searching.hash_table import HashTable


class TestHashMapMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.hash_table = HashTable()

    def test_hashmap_is_empty(self):
        """Testing hash map is_empty() method"""
        assert self.hash_table.is_empty()

    def test_hashmap_size(self):
        """Testing hash map size() method"""
        assert self.hash_table.size() == 0
        assert len(self.hash_table) == 0

    def test_hashmap_contains(self):
        """Testing hash map __contains__() method"""
        items = [
            (54, "cat"),
            (26, "dog"),
            (93, "lion"),
            (17, "tiger"),
            (77, "bird"),
            (31, "cow"),
            (44, "goat"),
            (55, "pig"),
            (20, "chicken"),
        ]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert 55 in self.hash_table
        assert 56 not in self.hash_table

    def test_hashmap_put(self):
        """Testing hash map put() method"""
        items = [
            (54, "cat"),
            (26, "dog"),
            (93, "lion"),
            (17, "tiger"),
            (77, "bird"),
            (31, "cow"),
            (44, "goat"),
            (55, "pig"),
            (20, "chicken"),
        ]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert self.hash_table.size() == 9

    def test_hashmap_put_error(self):
        """Testing hash map put() method exception"""
        with pytest.raises(Exception) as excinfo:
            for key in range(42):
                self.hash_table[key] = random.random()
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Hash Table is full"

    def test_hashmap_get(self):
        """Testing hash map get() method"""
        items = [
            (54, "cat"),
            (26, "dog"),
            (93, "lion"),
            (17, "tiger"),
            (77, "bird"),
            (31, "cow"),
            (44, "goat"),
            (55, "pig"),
            (20, "chicken"),
        ]
        for item in items:
            self.hash_table[item[0]] = item[1]
        assert self.hash_table[44] == "goat"
        assert self.hash_table[55] == "pig"

    def test_hashmap_get_error(self):
        """Testing hash map get() method exception"""
        items = [
            (54, "cat"),
            (26, "dog"),
            (93, "lion"),
            (17, "tiger"),
            (77, "bird"),
            (31, "cow"),
            (44, "goat"),
            (55, "pig"),
            (20, "chicken"),
        ]
        for item in items:
            self.hash_table[item[0]] = item[1]
        key = 1
        with pytest.raises(KeyError) as excinfo:
            self.hash_table.get(key)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "{} is not in the table".format(key)


if __name__ == "__main__":
    pytest.main(["test_hash_table.py"])
