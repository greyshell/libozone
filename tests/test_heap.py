#!/usr/bin/env python3

# author: greyshell
# command: poetry run python -m unittest discover -s tests/

import unittest
import operator

from libozone.priorityqueue.heap import Heap, HeapType


class Student:
    """helper class"""
    def __init__(self, name, score):
        self.name = name
        self.key = score

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


def is_heap_property_satisfied(array, heap_type=HeapType.MIN):
    """helper function to test the heap property"""
    for current_idx in range(1, len(array)):
        parent_idx = (current_idx - 1) // 2
        if heap_type == HeapType.MIN:
            if operator.gt(array[parent_idx], array[current_idx]):
                return False
        elif heap_type == HeapType.MAX:
            if operator.lt(array[parent_idx], array[current_idx]):
                return False
    return True


class TestProgram(unittest.TestCase):

    def test_heap_operations_01(self):
        """
        test a min heap operation
        """
        array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        heap = Heap(array, HeapType.MIN)

        # test the heap property
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MIN))

        # test insert()
        heap.insert(76)
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MIN))

        # test peek()
        self.assertEqual(-5, heap.peek())

        # test remove()
        self.assertEqual(-5, heap.remove())
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MIN))

        # test peek()
        self.assertEqual(2, heap.peek())

    def test_heap_operations_02(self):
        """
        test a min heap operation
        """
        array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        heap = Heap(array, HeapType.MAX)

        # test the heap property
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MAX))

        # test insert()
        heap.insert(76)
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MAX))

        # test peek()
        self.assertEqual(391, heap.peek())

        # test remove()
        self.assertEqual(391, heap.remove())
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MAX))

        # test peek()
        self.assertEqual(76, heap.peek())

    def test_heap_operations_03(self):
        """
        test a min heap operation
        """
        array = []
        heap = Heap(array, HeapType.MIN)

        # test the heap property
        self.assertEqual(True, is_heap_property_satisfied(array, heap_type=HeapType.MIN))

        with self.assertRaises(IndexError) as context:
            # Simulate a function or code that raises the error
            heap.peek()

        # Assert that the exception message matches
        self.assertEqual(str(context.exception), "empty heap")

        with self.assertRaises(IndexError) as context:
            # Simulate a function or code that raises the error
            heap.remove()

        # Assert that the exception message matches
        self.assertEqual(str(context.exception), "empty heap")

    def test_heap_operations_04(self):
        """
        test a min heap operation
        """
        alice = Student("alice", 80)
        bob = Student("bob", 90)
        malory = Student("malory", 95)
        tom = Student("malory", 55)

        arr = [alice, bob, malory, tom]
        heap = Heap(arr, HeapType.MAX)

        # test the heap property
        self.assertEqual(True, is_heap_property_satisfied(arr, heap_type=HeapType.MAX))

        # test peek()
        self.assertEqual(95, heap.peek().key)

        # test insert()
        chris = Student("chris", 98)
        heap.insert(chris)
        self.assertEqual(True, is_heap_property_satisfied(arr, heap_type=HeapType.MAX))

        # test peek()
        self.assertEqual(98, heap.peek().key)

        # test remove()
        self.assertEqual(98, heap.remove().key)
        self.assertEqual(True, is_heap_property_satisfied(arr, heap_type=HeapType.MAX))


if __name__ == '__main__':
    unittest.main()
