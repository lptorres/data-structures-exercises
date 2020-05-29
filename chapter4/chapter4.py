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
        node, self.head = self._head, self._head.link
        return node
