#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

from pythonds3.trees.binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):
    """
    This implementation of binary heap takes (key, value) pairs where key signifies priority
    We will assume that the keys are all comparable.
    """

    def change_priority(self, new_priority, value):
        """Change the priority"""
        key_to_move = 0
        for i in range(len(self._heap)):
            if self._heap[i][1] == value:
                key_to_move = i
                break
        if key_to_move > -1:
            self._heap[key_to_move] = (new_priority, self._heap[key_to_move][1])
            self._perc_up(key_to_move)
