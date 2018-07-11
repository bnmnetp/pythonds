'''
Testing the Priority Queue module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..')))

import pytest
from pythonds3.trees.priority_queue import PriorityQueue


class TestPriorityQueueMethods:
    
    @pytest.fixture(scope = 'function', autouse = True)
    def setup_class(cls):
        '''Setting up'''
        cls.priority_queue = PriorityQueue()
        cls.priority_queue.insert((2, 'x'))
        cls.priority_queue.insert((3, 'y'))
        cls.priority_queue.insert((5, 'z'))
        cls.priority_queue.insert((6, 'a'))
        cls.priority_queue.insert((4, 'd'))

    def test_delete(self):
        '''testing delete() method'''
        assert self.priority_queue.delete() == (2, 'x')
        assert self.priority_queue.delete() == (3, 'y')

    def test_decrease_key(self):
        '''Testing decrease_key() method'''
        self.priority_queue.change_priority(1, 'd')
        assert self.priority_queue.delete() == (1, 'd')

if __name__ == '__main__':
    pytest.main()
