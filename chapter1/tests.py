"""
Tests for chapter 1
"""
from math import gcd as pygcd
from random import randint
import unittest

from chapter1 import gcd, gcd2, gcd_recursive, LinkedList


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


class TestGCD2(unittest.TestCase):
    """Test the `chapter1.gcd2` function"""

    def test_gcd_book_example(self):
        """Test the gcd function using the example from the book:
        `m` = 608
        `n` = 133
        """
        GCD = gcd2(608, 133)
        self.assertEqual(GCD, 19)

    def test_gcd_random_small(self):
        """Test the gcd function using random integers until 1000."""
        m = randint(1, 1000)
        n = randint(1, 1000)
        GCD = gcd2(m, n)
        self.assertEqual(GCD, pygcd(m, n))

    def test_gcd_random_large(self):
        """Test the gcd function using random integers until 1 billion."""
        m = randint(1, 1000000000)
        n = randint(1, 1000000000)
        GCD = gcd2(m, n)
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


class TestLinkedList(unittest.TestCase):
    """Test the `chapter1.LinkedList` class"""
    def setUp(self):
        """Initialize a random integer generator"""
        self.random_ints = (randint(1, 1000000000) for _ in range(1, 1000))

    def test_prepend(self):
        """Test prepending"""
        my_list = LinkedList()
        python_list = []
        for i in self.random_ints:
            my_list.prepend(i)
            python_list.insert(0, i)
            self.assertEqual(my_list.head.info, python_list[0])

    def test_append(self):
        """Test appending"""
        my_list = LinkedList()
        python_list = []
        for i in self.random_ints:
            my_list.append(i)
            python_list.append(i)
            self.assertEqual(my_list.tail.info, python_list[-1])

    def test_len(self):
        """Test the length of the list"""
        my_list = LinkedList()
        python_list = []
        for i in self.random_ints:
            my_list.append(i)
            python_list.append(i)
            self.assertEqual(len(my_list), len(python_list))

    def test_elements(self):
        """Test the elements of the list"""
        python_list = [_ for _ in self.random_ints]
        my_list = LinkedList(python_list)
        cur = my_list.head
        for item in python_list:
            self.assertEqual(cur.info, item)
            cur = cur.link

    def test_getitem(self):
        """Test retrieval of individual items of the list"""
        python_list = [_ for _ in self.random_ints]
        my_list = LinkedList(python_list)
        for i in range(len(my_list)):
            self.assertEqual(my_list[i], python_list[i])

    def test_sort(self):
        """Test sorting on the list"""
        python_list = []
        my_list = LinkedList()
        for i in self.random_ints:
            python_list.append(i)
            python_list.sort()
            my_list.insert_sorted(i)
            self.assertEqual(str(my_list), str(python_list))


if __name__ == '__main__':
    # run all unit tests in this module
    unittest.main()
