"""
Chapter 5:
    - Queue implementation (using a linked list)
    - Deque implementation (using a linked list)
    - Topological sort
"""
from collections import defaultdict


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


class Queue:
    """Queue implementation using a linked list"""
    _front = None
    _rear = None
    __count = 0

    def __init__(self, items: list = []):
        """Initialize a queue.

        Keyword arguments:
        items - a list containing the elements
        """
        for item in items:
            self.enqueue(item)

    def __len__(self):
        """Return the length of the queue"""
        return self.__count

    @property
    def front(self):
        """Return the front of the queue"""
        return self._front

    @front.setter
    def front(self, node=None):
        """Set the front of the queue"""
        if node:
            assert type(node) == Node
        self._front = node

    @property
    def rear(self):
        """Return the rear of the queue"""
        return self._rear

    @rear.setter
    def rear(self, node=None):
        """Set the rear of the queue"""
        if node:
            assert type(node) == Node
        self._rear = node

    def enqueue(self, info: int):
        """Insert an element to the rear of the queue"""
        node = Node(info)
        if not self.front:
            # in the case of an empty queue
            self.front = node
            self.rear = node
        else:
            # non-empty queue
            self.rear.link = node
            self.rear = node
        self.__count += 1

    def dequeue(self):
        """Return and delete the front element"""
        if not self.front:
            raise IndexError("Deleting from empty queue")
        _front = self.front
        self.front = self.front.link
        self.__count -= 1
        return _front


def topological_sort(pairs_in: tuple):
    """Topological sort

    Keyword arguments:
    pairs_in -- iterable of tuples defining the partial ordering.
                The first item in the tuple represents an item, and the second
                item in the tuple represents the direct descendant.
    """
    def _build_partial_ordering():
        """Helper function to build the partial ordering as a dict"""
        out = defaultdict(lambda: {'count': 0, 'list': []})
        for node, descendant in pairs_in:
            out[node]['list'].insert(0, descendant)
            out[descendant]['count'] += 1
        return out

    # build the partial ordering
    partial_ordering = _build_partial_ordering()
    # initialize the output queue
    output = Queue()

    # Guard against circular dependencies
    if all([o['count'] > 0 for o in partial_ordering.values()]):
        return

    # Put initial (no predecessors) items into the output queue
    for k, info in partial_ordering.items():
        if info['count'] == 0:
            output.enqueue(k)

    while len(output) > 0:
        item = output.dequeue()
        descendants = partial_ordering[item.info]['list']
        print(item, end=' ')
        for desc in descendants:
            partial_ordering[desc]['count'] -= 1
            if partial_ordering[desc]['count'] == 0:
                output.enqueue(desc)
