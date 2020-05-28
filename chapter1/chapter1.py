"""
Chapter 1:
    - Euclid's Algorithm
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
    def __init__(self, info: int, link=None):
        """Initialize a Node.

        Keyword arguments:
        info -- the int data on this node
        link -- the next Node (if any) in the list
        """
        if link:
            assert type(link) == type(self)
        self.info = info
        self.link = link

    def __str__(self):
        """String representation of an instance"""
        return str(self.info)

    def set_link(self, link=None):
        """Set the value of self.link"""
        if link:
            assert type(link) == type(self)
        self.link = link


class LinkedList:
    """Class representing a linked list"""
    __head = None
    __tail = None
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
        cur = self.__head
        items = []
        while True:
            items.append(cur.info)
            if cur.link:
                cur = cur.link
            else:
                break
        return str(items)

    def __len__(self):
        """Return the length of the linked list"""
        return self.__count

    def __getitem__(self, index: int):
        """Return the element at the selected index"""
        if index >= self.__count:
            raise IndexError
        cur = self.__head
        for _ in range(index):
            cur = cur.link
        return cur.info

    def head(self):
        """Return the head of the linked list"""
        return self.__head

    def tail(self):
        """Return the tail of the linked list"""
        return self.__tail

    def append(self, info: int):
        """Insert an element at the end of the list"""
        node = Node(info)
        if not self.__head:
            self.__head = node
        else:
            cur = self.__head
            while cur.link:
                cur = cur.link
            cur.set_link(node)
        self.__tail = node
        self.__count += 1

    def prepend(self, info: int):
        """Insert an element at the start of the list"""
        node = Node(info)
        if not self.__head:
            self.__head = node
        else:
            node.set_link(self.__head)
            self.__head = node
        self.__count += 1

    def insert_sorted(self, info: int):
        """Insert an element into its sorted position in the list"""
        if not self.__head:
            self.append(info)
            return
        if info < self.__head.info:
            self.__head = Node(info, link=self.__head)
        else:
            cur = self.__head
            while cur.link and info > cur.link.info:
                cur = cur.link
            cur.link = Node(info, link=cur.link)
