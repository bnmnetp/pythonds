#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


from typing import Any


class Deque:
    """Dequeue implementation using a list"""

    def __init__(self) -> None:
        """Create new deque"""
        self._items: list[Any] = []

    def is_empty(self) -> bool:
        """Check if the deque is empty"""
        return not bool(self._items)

    def add_front(self, item: Any) -> None:
        """Add an item to the front of the deque"""
        self._items.append(item)

    def add_rear(self, item: Any) -> None:
        """Add an item to the rear of the deque"""
        self._items.insert(0, item)

    def remove_front(self) -> Any:
        """Remove an item from the front of the deque"""
        return self._items.pop()

    def remove_rear(self) -> Any:
        """Remove an item from the rear of the deque"""
        return self._items.pop(0)

    def size(self) -> int:
        """Get the number of items in the deque"""
        return len(self._items)
