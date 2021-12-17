#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


from typing import Any


class Stack:
    """Stack implementation using a list"""

    def __init__(self) -> None:
        """Create new stack"""
        self._items: list[Any] = []

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item: Any) -> None:
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self) -> Any:
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self) -> int:
        """Get the number of items in the stack"""
        return len(self._items)
