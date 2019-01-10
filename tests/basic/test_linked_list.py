#!/usr/bin/env python3
"""
Testing the Linked List module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
import pytest
from pythonds3.basic.linked_list import LinkedList
from pythonds3.basic.linked_list import LinkedListNode
from pythonds3.basic.linked_list import OrderedList
from pythonds3.basic.linked_list import UnorderedList


class TestLinkedListMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.node = LinkedListNode(42)
        self.list_ordered = OrderedList()
        self.list_unordered = UnorderedList()

    def test_node_init(self):
        """Testing node __init__ method"""
        assert self.node.data == 42

    # capsys fixture as parameter captures standard output
    def test_node_str(self, capsys):
        """Testing node __str__ method"""
        print(self.node)
        out, err = capsys.readouterr()
        assert out.strip() == "42"

    # xfail tests are expected to fail; should see a lowercase 'x' in output
    @pytest.mark.xfail(reason="TypeError: can't instantiate LinkedList (abstract)")
    def test_linked_list_fail(self):
        """Testing abstract linked list class"""
        LinkedList()

    def test_ordered_list_add(self):
        """Testing unordered list add method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_ordered.add(item)
            test_lst.insert(0, item)
        assert str(self.list_ordered) == str(sorted(test_lst))

    # Remove the following decorator once remove is implemented
    @pytest.mark.xfail(reason="remove() is an exercise")
    def test_ordered_list_remove(self):
        """Testing ordered list remove method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_ordered.add(item)
            test_lst.insert(0, item)
        assert str(self.list_ordered) == str(sorted(test_lst))

        self.list_ordered.remove(test_lst[0])
        test_lst.remove(test_lst[0])
        assert str(self.list_ordered) == str(sorted(test_lst))

        self.list_ordered.remove(test_lst[5])
        test_lst.remove(test_lst[5])
        assert str(self.list_ordered) == str(sorted(test_lst))

        self.list_ordered.remove(test_lst[-1])
        test_lst.remove(test_lst[-1])
        assert str(self.list_ordered) == str(sorted(test_lst))

    # remove() is an exercise, so this test is expected to fail only AFTER
    # remove() is implemented.
    # Switch following decorators after remove() is implemented.
    @pytest.mark.skip(reason="Only expected to fail AFTER remove() is written")
    # @pytest.mark.xfail(reason="42 shouldn't be found in the list")
    def test_ordered_list_remove_err(self):
        """Testing ordered list remove method exception"""
        for _ in range(10):
            self.list_ordered.add(random.randint(1, 10))
        # This should raise a ValueError
        self.list_ordered.remove(42)

    # Switch the following decorators once search() is implemented
    @pytest.mark.skip(reason="Only expected to fail AFTER search() is written")
    # @pytest.mark.xfail(reason="42 shouldn't be found in the list")
    def test_ordered_list_search(self):
        """Testing ordered list search method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_ordered.add(item)
            test_lst.insert(0, item)
        assert self.list_ordered.search(test_lst[0])
        assert self.list_ordered.search(test_lst[5])
        assert self.list_ordered.search(test_lst[-1])
        # This should raise an AssertionError
        assert self.list_ordered.search(42)

    def test_unordered_list_add(self):
        """Testing unordered list add method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_unordered.add(item)
            test_lst.insert(0, item)
        assert str(self.list_unordered) == str(test_lst)

    def test_unordered_list_remove(self):
        """Testing unordered list remove method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_unordered.add(item)
            test_lst.insert(0, item)
        assert str(self.list_unordered) == str(test_lst)
        self.list_unordered.remove(test_lst[0])
        test_lst.remove(test_lst[0])
        assert str(self.list_unordered) == str(test_lst)
        self.list_unordered.remove(test_lst[5])
        test_lst.remove(test_lst[5])
        assert str(self.list_unordered) == str(test_lst)
        self.list_unordered.remove(test_lst[-1])
        test_lst.remove(test_lst[-1])
        assert str(self.list_unordered) == str(test_lst)

    # This test should fail due to a ValueError raised when value not in list
    def test_unordered_list_remove_err(self):
        """Testing unordered list remove method exception"""
        for _ in range(10):
            self.list_unordered.add(random.randint(1, 10))
        value = 42
        with pytest.raises(ValueError) as excinfo:
            self.list_unordered.remove(value)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "{} is not in the list".format(value)

    # This test should fail because 42 is not in the list
    def test_unordered_list_search(self):
        """Testing unordered list search method"""
        test_lst = []
        for _ in range(10):
            item = random.randint(1, 10)
            self.list_unordered.add(item)
            test_lst.insert(0, item)
        assert self.list_unordered.search(test_lst[0])
        assert self.list_unordered.search(test_lst[5])
        assert self.list_unordered.search(test_lst[-1])
        with pytest.raises(AssertionError):
            assert self.list_unordered.search(42)

    def test_linked_list_str(self, capsys):
        """Testing unordered list __str__ method"""
        int_value = 42
        str_value = "hello"
        self.list_unordered.add(int_value)
        self.list_unordered.add(str_value)
        print(self.list_unordered)
        out, err = capsys.readouterr()
        assert out.strip() == "[{}, {}]".format(str_value, int_value)


if __name__ == "__main__":
    pytest.main(["test_linked_list.py"])
