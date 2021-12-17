#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


from typing import Any


class Queue:
    """Queue implementation using a list"""

    def __init__(self) -> None:
        """Create new queue"""
        self._items: list[Any] = []

    def is_empty(self) -> bool:
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item: Any) -> None:
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self) -> Any:
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self) -> int:
        """Get the number of items in the queue"""
        return len(self._items)
