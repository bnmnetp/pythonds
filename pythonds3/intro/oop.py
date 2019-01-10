#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""


def gcd(number1, number2):
    """Helper function to simplify fractions"""
    if not isinstance(number1, int) or not isinstance(number2, int):
        raise TypeError("Numerator and denominator must be integers")
    while number1 % number2:
        number1, number2 = number2, number1 % number2
    return number2


class Fraction:
    """Fraction class"""

    def __init__(self, new_numer, new_denom):
        try:
            common = gcd(new_numer, new_denom)
        except TypeError:
            raise
        self._numer = new_numer // common
        self._denom = new_denom // common

    @property
    def numer(self):
        """Get numerator"""
        return self._numer

    @numer.setter
    def set_numer(self, new_numer):
        """Set numerator"""
        self._numer = new_numer

    def get_denom(self):
        """Get deniminator"""
        return self._denom

    def set_denom(self, new_denom):
        """Set deniminator"""
        self._denom = new_denom

    # Another way to create an attribute
    denom = property(get_denom, set_denom)

    def __str__(self):
        """Get the string value"""
        if self._numer > self._denom:
            return "{} {}/{}".format(
                self._numer // self._denom, self._numer % self._denom, self._denom
            )
        return "{}/{}".format(self._numer, self._denom)

    def __repr__(self):
        """Fraction representation"""
        return "Fraction({}, {})".format(self._numer, self._denom)

    def __eq__(self, other):
        """Equality comparison"""
        return self._numer * other.denom == other.numer * self._denom

    def __add__(self, other):
        """Add two fractions"""
        new_numer = self._numer * other.denom + self._denom * other.numer
        new_denom = self._denom * other.denom
        return Fraction(new_numer, new_denom)
