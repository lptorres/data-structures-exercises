"""
Chapter 4:
    - Stack implementation (using a linked list)
    - Converting infix expressions to postfix form
    - Evaluating postfix expressions
"""


class Node:
    """Class representing an element in a linked list"""
    _info = 0
    _link = None

    def __init__(self, info: str, link=None):
        """Initialize a Node.

        Keyword arguments:
        info -- the str data on this node
        link -- the next Node (if any) in the list
        """
        if link:
            assert type(link) == type(self)
        self._info = info
        self._link = link

    def __str__(self):
        """String representation of an instance"""
        return str(self.info)

    @property
    def info(self):
        """Getter for info"""
        return self._info

    @info.setter
    def info(self, value):
        """Setter for info"""
        assert type(value) == str
        self._info = value

    @property
    def link(self):
        """Getter for link"""
        return self._link

    @link.setter
    def link(self, link=None):
        """Setter for link"""
        if link:
            assert type(link) == type(self)
        self._link = link


class Stack:
    """Stack implementation using a linked list"""
    _head = None

    def __init__(self, items: list = []):
        """Initialize a linked list.

        Keyword arguments:
        items - a list containing the elements
        """
        for item in items:
            self.push(item)

    @property
    def head(self):
        """Get the head of the stack without removing it"""
        if self._head:
            _head = self.pop()
            self.push(_head)
            return _head

    @head.setter
    def head(self, node=None):
        """Set the head of the linked list"""
        if node:
            assert type(node) == Node
        self._head = node

    def push(self, info: str):
        """Push an element to the top of the stack"""
        node = Node(info)
        if not self._head:
            self.head = node
        else:
            node.link = self._head
            self.head = node

    def pop(self):
        """Remove the top of the stack"""
        if self._head is None:
            raise IndexError("pop from empty stack")
        node, self.head = self._head, self._head.link
        return node


def is_palindrome(s):
    """Check if a string is a palindrome or not.

    In the book, the definition of a palindrome is simplified. The alphabet
    is only {'a', 'b'} and 'c' denotes the middle of the string. Examples:
    'c', 'aca', 'bcb', 'abbcbba', 'baacaab', etc. Examples of trings which are
    not palindromes according to this definition are: 'abba', 'abaabcbabba',
    'abacab', 'bbaacaabbb', etc.
    Note: The algorithm is not very pythonic, but the purpose of the
    exercise is to illustrate the use of Stacks to check for palindromes.
    """
    if 'c' not in s:
        return False
    stack = Stack()
    firsthalf = True
    for letter in s:
        if letter == 'c':
            firsthalf = False
            continue
        if firsthalf:
            stack.push(letter)
        else:
            try:
                if letter != str(stack.pop()):
                    return False
            except IndexError:
                return False
    return True


def is_palindrome2(s):
    """Check if a string is a palindrome or not.

    This is a pythonic implementation of palindrome checking given the same
    problem definition of a palindrome, but without using stacks.
    """
    return ('c' in s and s == s[::-1])


def polish(s):
    """Generate the postfix (Reverse Polish) form of an infix expression.

    The infix expression may only contain the five binary arithmetic operators
    +, -, *, /, and ^.
    """
    def _is_operator(t):
        return t in ('+', '-', '*', '/', '^')

    def _icp(t):
        """Determine the in-coming priority of a token"""
        if t == '^':
            return 6
        elif t in ('*', '/'):
            return 3
        elif t in ('+', '-'):
            return 1

    def _isp(t):
        """Determine the in-stack priority of a token"""
        if t == '^':
            return 5
        elif t in ('*', '/'):
            return 4
        elif t in ('+', '-'):
            return 2
        elif t == '(':
            return 0
    output = ''
    stack = Stack()
    for token in s:
        if token == '(':
            stack.push(token)
        elif token == ')':
            try:
                while (popped := str(stack.pop())) != '(':
                    output += popped
            except IndexError:
                return output
        elif _is_operator(token):
            while (h := stack.head) and _icp(token) < _isp(str(h)):
                output += str(stack.pop())
            stack.push(token)
        else:
            output += token
    while stack.head:
        output += str(stack.pop())
    return output
