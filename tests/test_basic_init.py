#!/usr/bin/env python3
"""
Testing the basic __init__ file
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.basic import Deque
from pythonds3.basic import OrderedList
from pythonds3.basic import Queue
from pythonds3.basic import Stack
from pythonds3.basic import UnorderedList

data_structures = {
    "stack": Stack(),
    "queue": Queue(),
    "deque": Deque(),
    "olist": OrderedList(),
    "ulist": UnorderedList(),
}

# Setup
@pytest.fixture(params=data_structures)
def set_up(request):
    """Setting up"""
    return data_structures[request.param]


# Test if new instances of these ds's are empty
def test_is_empty(set_up):
    assert set_up.is_empty()


if __name__ == "__main__":
    pytest.main(["test_basic_init.py"])
