'''
Testing the graphs __init__ file
Roman Yasinovskyy, 2017
'''

import unittest
from graphs import Graph


class TestGraphsInit(unittest.TestCase):
    '''Testing the graphs __init__ file'''
    def setUp(self):
        '''Setting up'''
        self._graph = Graph()

    def test_len(self):
        '''Testing len() method'''
        self.assertEqual(len(self._graph), 0)

if __name__ == '__main__':
    unittest.main()
