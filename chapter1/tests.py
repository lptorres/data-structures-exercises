"""
Test class for chapter 1
"""
from math import gcd as pygcd
from random import randint
import unittest

from chapter1 import gcd, gcd_recursive


class TestGCD(unittest.TestCase):
    """Test the `chapter1.gcd` function"""

    def test_gcd_book_example(self):
        """Test the gcd function using the example from the book:
        `m` = 608
        `n` = 133
        """
        GCD = gcd(608, 133)
        self.assertEqual(GCD, 19)

    def test_gcd_random_small(self):
        """Test the gcd function using random integers until 1000."""
        m = randint(1, 1000)
        n = randint(1, 1000)
        GCD = gcd(m, n)
        self.assertEqual(GCD, pygcd(m, n))

    def test_gcd_random_large(self):
        """Test the gcd function using random integers until 1 billion."""
        m = randint(1, 1000000000)
        n = randint(1, 1000000000)
        GCD = gcd(m, n)
        self.assertEqual(GCD, pygcd(m, n))


class TestGCDRecursive(unittest.TestCase):
    """Test the `chapter1.gcd_recursive` function"""

    def test_gcd_book_example(self):
        """Test the gcd function using the example from the book:
        `m` = 608
        `n` = 133
        """
        GCD = gcd_recursive(608, 133)
        self.assertEqual(GCD, 19)

    def test_gcd_random_small(self):
        """Test the gcd function using random integers until 1000."""
        m = randint(1, 1000)
        n = randint(1, 1000)
        GCD = gcd_recursive(m, n)
        self.assertEqual(GCD, pygcd(m, n))

    def test_gcd_random_large(self):
        """Test the gcd function using random integers until 1 billion."""
        m = randint(1, 1000000000)
        n = randint(1, 1000000000)
        GCD = gcd_recursive(m, n)
        self.assertEqual(GCD, pygcd(m, n))


if __name__ == '__main__':
    # run all unit tests in this module
    unittest.main()
