'''
Testing the Priority Queue module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
'''

#!/usr/bin/env python3

# Specifies the absolute path to the pythonds3 module
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pythonds3.trees.priority_queue import PriorityQueue


class TestPriorityQueueMethods:
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        '''Setting up'''
        self.priority_queue = PriorityQueue()
        self.priority_queue.insert((2, 'x'))
        self.priority_queue.insert((3, 'y'))
        self.priority_queue.insert((5, 'z'))
        self.priority_queue.insert((6, 'a'))
        self.priority_queue.insert((4, 'd'))

    def test_delete(self):
        '''testing delete() method'''
        assert self.priority_queue.delete() == (2, 'x')
        assert self.priority_queue.delete() == (3, 'y')

    def test_decrease_key(self):
        '''Testing decrease_key() method'''
        self.priority_queue.change_priority(1, 'd')
        assert self.priority_queue.delete() == (1, 'd')

if __name__ == '__main__':
    pytest.main(['test_priority_queue.py'])
