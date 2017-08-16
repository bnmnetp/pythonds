'''
Testing the OOP module
Roman Yasinovskyy, 2017
'''

#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from oop import Fraction


class TestOOPMethods(unittest.TestCase):
    '''Testing OOP'''

    def setUp(self):
        '''Setting up'''
        self.frac1 = Fraction(1, 3)
        self.frac2 = Fraction(4, 6)
        self.frac3 = Fraction(6, 4)

    def test_init(self):
        '''Testing init'''
        self.assertEqual(self.frac1, Fraction(1, 3))

    def test_init_simplification(self):
        '''Testing init with gcd'''
        self.assertEqual(self.frac2, Fraction(2, 3))

    def test_init_numer_error(self):
        '''Testing TypeError'''
        self.assertRaises(TypeError, Fraction, *(1.5, 2))

    def test_init_numer_error_2(self):
        '''Testing TypeError'''
        self.assertRaises(TypeError, Fraction, *('1', 2))

    def test_init_denom_error(self):
        '''Testing TypeError'''
        self.assertRaises(TypeError, Fraction, *(1, 2.5))

    def test_init_denom_error_2(self):
        '''Testing TypeError'''
        self.assertRaises(TypeError, Fraction, *(1, '2'))

    def test_get_numer(self):
        '''Testing numerator getter'''
        self.assertEqual(self.frac1.numer, 1)

    def test_get_denom(self):
        '''Testing denominator getter'''
        self.assertEqual(self.frac1.denom, 3)

    def test_fractions_add(self):
        '''Testing __add__ method'''
        self.assertEqual(self.frac1 + self.frac2, Fraction(1, 1))

    # Remove this decorator once __sub__ is implemented
    @unittest.expectedFailure
    def test_fractions_sub(self):
        '''Testing __sub__ method'''
        self.assertEqual(self.frac1 - self.frac2, Fraction(-1, 3))

    # Remove this decorator once __mult__ is implemented
    @unittest.expectedFailure
    def test_fractions_mult(self):
        '''Testing __mult__ method'''
        self.assertEqual(self.frac1 * self.frac2, Fraction(2, 9))

    # Remove this decorator once __truediv__ is implemented
    @unittest.expectedFailure
    def test_fractions_truediv(self):
        '''Testing __truediv__ method'''
        self.assertEqual(self.frac1 / self.frac2, Fraction(1, 2))

    def test_str(self):
        '''Testing __str__method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(self.frac3)
        self.assertEqual(output.getvalue().strip(), '1 1/2')

    def test_repr(self):
        '''Testing __repr__method'''
        with patch('sys.stdout', new=StringIO()) as output:
            print(repr(self.frac3))
        self.assertEqual(output.getvalue().strip(), 'Fraction(3, 2)')

if __name__ == '__main__':
    unittest.main()
