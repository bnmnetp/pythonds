'''
Testing the basic __init__ file
Roman Yasinovskyy, 2017
'''

import unittest
from basic import *
#from pythonds.basic import *


class TestBasicsInit(unittest.TestCase):
    '''Testing the basic __init__ file'''

    def setUp(self):
        '''Setting up'''
        self._stack = Stack()
        self._queue = Queue()
        self._deque = Deque()
        self._olist = OrderedList()
        self._ulist = UnorderedList()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        self.assertTrue(self._stack.is_empty())
        self.assertTrue(self._queue.is_empty())
        self.assertTrue(self._deque.is_empty())
        self.assertTrue(self._olist.is_empty())
        self.assertTrue(self._ulist.is_empty())

    def tearDown(self):
        '''Tearing down'''
        del self._stack
        del self._queue
        del self._deque
        del self._olist
        del self._ulist

if __name__ == '__main__':
    unittest.main(verbosity=2)
