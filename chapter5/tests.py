""" Tests for chapter 5"""
import unittest

from chapter5 import Queue


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


if __name__ == '__main__':
    unittest.main()
