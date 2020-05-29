""" Tests for chapter 4"""
from string import ascii_letters
import unittest

from chapter4 import Stack


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


if __name__ == '__main__':
    unittest.main()
