""" Tests for chapter 4"""
from random import choices, randint
from string import ascii_letters
import unittest

from chapter4 import Stack, is_palindrome, is_palindrome2, polish, evaluate


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
        """Generate a palindrome (or not)"""
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


class TestPolish(unittest.TestCase):
    """Test the `chapter4.polish` function"""
    expressions = [
        ("ABCD-E2^/+*F+", "(A*(B+(C-D)/E^2)+F)"),
        ("ABC*DE*/+", "A+B*C/(D*E)"),
        ("BD2^^CE^/", "B^D^2/C^E"),
        ("AB6D+E-*8/*G3^-", "A*(B*(6+D-E)/8)-G^3"),
        ("AXBXCXD*+*+*+", "A+X*(B+X*(C+X*D))"),
        ("ABC+D^/E*FG-/H*", "A/(B+C)^D*E/(F-G)*H"),
        ("AB-CD-2^F+*G12/^/", "((A-B)*((C-D)^2+F)/G^(1/2))")
    ]

    def test_polish(self):
        for postfix, infix in self.expressions:
            self.assertEqual(polish(infix), postfix)


class TestEvaluate(unittest.TestCase):
    """Test the `chapter4.evaluate` function"""
    expressions = [
        ("ABCD-E2^/+*F+", -41.4375),
        ("ABC*DE*/+", 0.33333333333333304),
        ("BD2^^CE^/", -9851.954833984375),
        ("AB6D+E-*8/*G3^-", -237.875),
        ("AXBXCXD*+*+*+", 3735.0),
        ("ABC+D^/E*FG-/H*", -12.857142857142858),
        ("AB-CD-2^F+*G12/^/", 83.28265125462806)
    ]
    values = {
        'A': 5,
        'B': -7,
        'C': 8,
        'D': 3,
        'E': 4,
        'F': -8,
        'G': 6,
        'H': 9,
        'X': 10
    }

    def test_evaluate(self):
        for postfix, value in self.expressions:
            self.assertEqual(evaluate(postfix, self.values), value)


if __name__ == '__main__':
    unittest.main()
