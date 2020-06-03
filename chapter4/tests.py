""" Tests for chapter 4"""
from random import choices, randint
from string import ascii_letters
import unittest

from chapter4 import Stack, is_palindrome, is_palindrome2


class TestStack(unittest.TestCase):
    """Test the `chapter4.Stack` data structure"""
    def test_push(self):
        """Test pushing into the stack"""
        stack = Stack()
        for letter in ascii_letters:
            stack.push(letter)
            self.assertEqual(str(stack._head), letter)

    def test_pop(self):
        """Test popping from the stack"""
        stack = Stack()
        for letter in ascii_letters:
            stack.push(letter)

        # Stacks are LIFO, should check against the reversed `ascii_letters`
        for letter in reversed(ascii_letters):
            self.assertEqual(str(stack.pop()), letter)

    def test_head(self):
        """Test the head"""
        stack = Stack()
        # The head should always be the most recently pushed item
        for letter in ascii_letters:
            stack.push(letter)
            self.assertEqual(str(stack.head), letter)

        # Head shouldn't remove elements from the stack,
        # so they should all still be in the stack when popping
        for letter in reversed(ascii_letters):
            self.assertEqual(str(stack.pop()), letter)


class TestIsPalindrome(unittest.TestCase):
    """Test the `chapter4.is_palindrome` function"""
    def generate_palindrome(self, force_palindrome=True):
        half = ''.join(choices(['a', 'b'], k=randint(1, 500000)))
        if force_palindrome:
            return f"{half}c{half[::-1]}"
        else:
            i = randint(0, len(half))
            return f"{half[:i]}c{half[i:]}"

    def test_is_palindrome(self):
        """Test the `is_palindrome` function using a random string"""
        for force_palindrome in (True, False):
            s = self.generate_palindrome(force_palindrome)
            self.assertEqual(
                is_palindrome2(s),
                is_palindrome(s),
                msg=f"{s}"
            )


if __name__ == '__main__':
    unittest.main()
