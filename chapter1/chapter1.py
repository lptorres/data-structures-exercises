"""
Chapter 1:
    - Euclid's Algorithm
    - Linked List implementation
"""


def gcd(m: int, n: int):
    """Euclid's algorithm for finding the greatest common divisor (GCD) of two
    positive integers _m_ and _n_.
    """
    while True:
        r = m % n
        if r == 0:
            break
        m = n
        n = r
    return n


def gcd2(m: int, n: int):
    """Euclid's algorithm using Python3.8's walrus assignment"""
    while (r := m % n) != 0:
        m = n
        n = r
    return n


def gcd_recursive(m: int, n: int):
    """Recursive implementation of Euclid's algorithm"""
    r = m % n
    if r == 0:
        return n
    return gcd_recursive(m=n, n=r)


class Node:
    """Class representing an element in a linked list"""
    _info = 0
    _link = None

    def __init__(self, info: int, link=None):
        """Initialize a Node.

        Keyword arguments:
        info -- the int data on this node
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
        assert type(value) == int
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


class LinkedList:
    """Class representing a linked list"""
    _head = None
    _tail = None
    __count = 0

    def __init__(self, items: list = []):
        """Initialize a linked list.

        Keyword arguments:
        items - a list containing the elements
        """
        for item in items:
            self.append(item)

    def __str__(self):
        """Return the string representation of the linked list"""
        items = []
        cur = self.head
        while cur:
            items.append(cur.info)
            cur = cur.link
        return str(items)

    def __len__(self):
        """Return the length of the linked list"""
        return self.__count

    def __getitem__(self, index: int):
        """Return the element at the selected index"""
        if index >= self.__count:
            raise IndexError
        cur = self.head
        for _ in range(index):
            cur = cur.link
        return cur.info

    @property
    def head(self):
        """Return the head of the linked list"""
        return self._head

    @head.setter
    def head(self, node=None):
        """Set the head of the linked list"""
        if node:
            assert type(node) == Node
        self._head = node

    @property
    def tail(self):
        """Return the tail of the linked list"""
        return self._tail

    @tail.setter
    def tail(self, node=None):
        """Set the tail of the linked list"""
        if node:
            assert type(node) == Node
        self._tail = node

    def append(self, info: int):
        """Insert an element at the end of the list"""
        node = Node(info)
        if (cur := self.head):
            while cur.link:
                cur = cur.link
            cur.link = node
        else:
            self.head = node
        self.tail = node
        self.__count += 1

    def prepend(self, info: int):
        """Insert an element at the start of the list"""
        node = Node(info)
        if not self.head:
            self.head = node
        else:
            node.link = self.head
            self.head = node
        self.__count += 1

    def insert_sorted(self, info: int):
        """Insert an element into its sorted position in the list"""
        if (cur := self.head):
            if info < cur.info:
                self.head = Node(info, link=cur)
            else:
                while cur.link and info > cur.link.info:
                    cur = cur.link
                cur.link = Node(info, link=cur.link)
        else:
            self.append(info)
