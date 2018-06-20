'''
Testing the search __init__ file
Roman Yasinovskyy, 2017
'''

import unittest
from pythonds3.searching import HashTable


class TestSearchInit(unittest.TestCase):
    '''Testing the search __init__ file'''

    def setUp(self):
        '''Setting up'''
        self._hash_table = HashTable()

    def test_len(self):
        '''Testing len() method'''
        self.assertEqual(len(self._hash_table), 0)

if __name__ == '__main__':
    unittest.main()
