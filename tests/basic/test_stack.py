'''
Testing the Stack module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '..')))

import pytest
from pythonds3.basic.stack import Stack


class TestStackMethods:

    @pytest.fixture(scope = 'function', autouse = True)
    def setup_class(cls):
        '''Setting up'''
        cls.stack = Stack()

    def test_is_empty(self):
        '''Testing is_empty() method'''
        assert self.stack.is_empty()
        self.stack.push(42)
        assert not self.stack.is_empty()

    def test_size(self):
        '''Testing size() method'''
        assert self.stack.size() == 0
        self.stack.push(42)
        assert self.stack.size() == 1

    def test_push(self):
        '''Testing push() method'''
        self.stack.push(42)
        assert self.stack.size() == 1

    def test_pop(self):
        '''Testing pop() method'''
        self.stack.push(42)
        assert self.stack.pop() == 42
        assert self.stack.is_empty()

    def test_peek(self):
        '''Testing peek() method'''
        self.stack.push(42)
        assert self.stack.peek() == 42
        assert self.stack.size() == 1

if __name__ == '__main__':
    pytest.main()
