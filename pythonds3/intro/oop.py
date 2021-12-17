#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


from math import gcd


class Fraction:
    """Fraction class"""

    def __init__(self, new_numer: int, new_denom: int) -> None:
        """Create new fraction"""
        if not isinstance(new_numer, int) or not isinstance(new_denom, int):
            raise TypeError("Numerator and denominator must be integers")
        common = gcd(new_numer, new_denom)
        self._numer = new_numer // common
        self._denom = new_denom // common

    @property
    def numer(self) -> int:
        """Get numerator"""
        return self._numer

    @numer.setter
    def numer(self, new_numer: int) -> None:
        """Set numerator"""
        self._numer = new_numer

    def get_denom(self) -> int:
        """Get deniminator"""
        return self._denom

    def set_denom(self, new_denom: int) -> None:
        """Set deniminator"""
        self._denom = new_denom

    # Another way to create an attribute
    denom = property(get_denom, set_denom)

    def __str__(self) -> str:
        """Get the string value"""
        if self._numer > self._denom:
            return f"{self._numer // self._denom} {self._numer % self._denom}/{self._denom}"
        return f"{self._numer}/{self._denom}"

    def __repr__(self) -> str:
        """Fraction representation"""
        return f"Fraction({self._numer}, {self._denom})"

    def __eq__(self, other) -> bool:
        """Equality comparison"""
        if not isinstance(other, Fraction):
            return NotImplemented
        return self._numer * other.denom == other.numer * self._denom

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add two fractions"""
        new_numer = self._numer * other.denom + self._denom * other.numer
        new_denom = self._denom * other.denom
        return Fraction(new_numer, new_denom)
