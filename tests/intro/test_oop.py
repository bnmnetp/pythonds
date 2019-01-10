#!/usr/bin/env python3
"""
Testing the OOP module
Roman Yasinovskyy, 2017
Karina E. Hoff, 2018
"""


# Specifies the absolute path to the pythonds3 module
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pythonds3.intro.oop import Fraction


class TestOOPMethods:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Setting up"""
        self.frac1 = Fraction(1, 3)
        self.frac2 = Fraction(4, 6)
        self.frac3 = Fraction(6, 4)

    def test_init(self):
        """Testing init"""
        assert self.frac1 == Fraction(1, 3)

    def test_init_simplification(self):
        """Testing init with gcd"""
        assert self.frac2 == Fraction(2, 3)

    # Fails because you cannot create a fraction with float as numerator
    def test_init_numer_error(self):
        """Testing TypeError"""
        with pytest.raises(TypeError) as excinfo:
            Fraction(1.5, 2)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numerator and denominator must be integers"

    # Fails because you cannot create a fraction with str as numerator
    def test_init_numer_error_2(self):
        """Testing TypeError"""
        with pytest.raises(TypeError) as excinfo:
            Fraction("1", 2)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numerator and denominator must be integers"

    # Fails because you cannot create a fraction with a float as denominator
    def test_init_denom_error(self):
        """Testing TypeError"""
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, 2.5)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numerator and denominator must be integers"

    # Fails because you cannot create a fraction with str as denominator
    def test_init_denom_error_2(self):
        """Testing TypeError"""
        with pytest.raises(TypeError) as excinfo:
            Fraction(1, "2")
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numerator and denominator must be integers"

    def test_get_numer(self):
        """Testing numerator getter"""
        assert self.frac1.numer == 1

    def test_get_denom(self):
        """Testing denominator getter"""
        assert self.frac1.denom == 3

    def test_fractions_add(self):
        """Testing __add__ method"""
        assert self.frac1 + self.frac2 == Fraction(1, 1)

    # Remove this decorator once __sub__ is implemented
    @pytest.mark.skip(reason="__sub__ is not implemented")
    def test_fractions_sub(self):
        """Testing __sub__ method"""
        assert self.frac1 - self.frac2 == Fraction(-1, 3)

    # Remove this decorator once __mult__ is implemented
    @pytest.mark.skip(reason="__mult__ is not implemented")
    def test_fractions_mult(self):
        """Testing __mult__ method"""
        assert self.frac1 * self.frac2 == Fraction(2, 9)

    # Remove this decorator once __truediv__ is implemented
    @pytest.mark.skip(reason="__truediv__ is not implemented")
    def test_fractions_truediv(self):
        """Testing __truediv__ method"""
        assert self.frac1 / self.frac2 == Fraction(1, 2)

    def test_str(self, capsys):
        """Testing __str__method"""
        print(self.frac3)
        out, err = capsys.readouterr()
        assert out.strip() == "1 1/2"

    def test_repr(self, capsys):
        """Testing __repr__method"""
        print(repr(self.frac3))
        out, err = capsys.readouterr()
        assert out.strip() == "Fraction(3, 2)"


if __name__ == "__main__":
    pytest.main(["test_oop.py"])
