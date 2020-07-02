""" Tests for chapter 5"""
import unittest

from chapter5 import Queue, topological_sort


class TestQueue(unittest.TestCase):
    """Test the `chapter5.Queue` data structure"""
    def test_enqueue(self):
        """Test enqueueing"""
        queue = Queue()
        for i in range(1000):
            queue.enqueue(i)
            self.assertEqual(queue.front.info, 0)
            self.assertEqual(queue.rear.info, i)
            self.assertEqual(len(queue), i+1)

    def test_dequeue(self):
        """Test dequeueing"""
        queue = Queue(list(range(1, 1001)))
        for i in range(1, 1001):
            self.assertEqual(queue.dequeue().info, i)
            self.assertEqual(len(queue), 1000-i)
            if queue.front:
                self.assertEqual(queue.front.info, i+1)


class TestTopoSort(unittest.TestCase):
    """Test the `chapter5.topological_sort` function """
    def test_toposort(self):
        """Test toposort with the chapter example"""
        order = (
            (1, 2),
            (2, 3),
            (4, 5),
            (5, 1),
            (5, 12),
            (5, 6),
            (7, 6),
            (8, 9),
            (10, 11),
            (12, 10),
            (12, 13),
            (13, 14),
            (13, 9),
            (14, 15)
        )
        ordering = topological_sort(order)
        self.assertIn(ordering, [
            # Possible valid orderings
            [4, 7, 8, 5, 6, 12, 1, 13, 10, 2, 9, 14, 11, 3, 15],
            [4, 5, 1, 12, 10, 13, 2, 3, 11, 14, 7, 6, 8, 9, 15],
            [4, 5, 12, 1, 10, 2, 13, 8, 11, 14, 7, 3, 9, 15, 6]
        ])


if __name__ == '__main__':
    unittest.main()
