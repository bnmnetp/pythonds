#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


class HashTable:
    """Hash Table implementation"""

    def __init__(self, size=16):
        """Create a hash table"""
        self._size = size
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def __getitem__(self, key):
        """Magic __get__"""
        return self.get(key)

    def __setitem__(self, key, data):
        """Magic __set__"""
        self.put(key, data)

    def __len__(self):
        """Magic __len__"""
        return self._size - self._slots.count(None)

    def __contains__(self, key):
        """Magin in"""
        return key in self._slots

    def _hash_function(self, key, size):
        """Simple hash function"""
        return key % size

    def _rehash(self, old_hash, size, step=1):
        """Simple rehash function"""
        return (old_hash + step) % size

    def is_empty(self):
        """Check if the table is empty"""
        return self._size == self._slots.count(None)

    def size(self):
        """Get number of items in the table"""
        return self._size - self._slots.count(None)

    def put(self, key, data):
        """Add an item to the table"""
        hash_value = self._hash_function(key, len(self._slots))

        if self._slots[hash_value] is None:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            if self._slots[hash_value] == key:
                self._data[hash_value] = data  # replace
            else:
                j = 0
                next_slot = self._rehash(hash_value, len(self._slots), j)
                while (
                    self._slots[next_slot] is not None
                    and self._slots[next_slot] != key
                    and j < self._size
                ):
                    j = j + 1
                    next_slot = self._rehash(hash_value, len(self._slots), j)

                if self._slots[next_slot] is None:
                    self._slots[next_slot] = key
                    self._data[next_slot] = data
                elif j == self._size:
                    raise Exception("Hash Table is full")
                else:
                    self._data[next_slot] = data  # replace

    def get(self, key):
        """Get an item from the table"""
        start_slot = self._hash_function(key, len(self._slots))
        position = start_slot
        j = 0

        while self._slots[position] is not None and j < self._size:
            if self._slots[position] == key:
                return self._data[position]
            j = j + 1
            position = self._rehash(start_slot, len(self._slots), j)

        raise KeyError("{} is not in the table".format(key))
