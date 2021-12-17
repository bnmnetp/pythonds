#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

from typing import Any
from pythonds3.trees.binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):
    """
    This implementation of binary heap takes (priority, key) pairs
    We will assume that the priorities are all comparable.
    """

    def change_priority(self, search_key: Any, new_priority: Any) -> None:
        """Change the priority"""
        key_to_move = -1
        for i, (_, key) in enumerate(self._heap):
            if key == search_key:
                key_to_move = i
                break
        if key_to_move > -1:
            self._heap[key_to_move] = (new_priority, search_key)
            self._perc_up(key_to_move)

    def __contains__(self, search_key: Any) -> bool:
        """Find a key in the queue"""
        for _, key in self._heap:
            if key == search_key:
                return True
        return False
