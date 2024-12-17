# Heap

## API Details

| Usage                                       | Function                | Time      | Space |
|---------------------------------------------|-------------------------|-----------|-------|
| Build a max heap from an array              | Heap(arr, HeapType.MAX) | O(N*logN) | O(1)  |
| Build a min heap from an array              | Heap(arr, HeapType.MIN) | O(N*logN) | O(1)  |
| Peek an element from the heap               | peek()                  | O(1)      | O(1)  |
| Insert an element into heap(`heapify_up`)   | insert(element)         | O(logN)   | O(1)  |
| Remove an element into heap(`heapify_down`) | remove()                | O(logN)   | O(1)  |




## Example

```python
#!/usr/bin/env python3
# description: demo heap
# author: greyshell

from libozone import Heap, HeapType


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


if __name__ == '__main__':
    arr = [5, 9, 2]

    hmin = Heap(arr)  # create a min heap
    print(hmin.peek())  # peek the min item from the heap
    hmin.insert(1)  # insert an item into the heap
    print(hmin.remove())  # remove an item from the heap
    print(hmin)  # print all items from the heap
    print(len(hmin))  # print the length of the heap

    hmax = Heap(arr, HeapType.MAX)  # create a max heap
    print(hmax.peek())  # peek the max item from the heap
    hmax.insert(1)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap

    alice = Student(name="alice", score=80)
    bob = Student("bob", 90)
    malory = Student("malory", 75)
    tom = Student("tom", 85)
    
    arr = [alice, bob, malory, tom]
    heap = Heap(arr, HeapType.MAX)
    print(hmax.peek().key)  # peek the max item from the heap -> 90
    ram = Student("ram", 95)
    hmax.insert(ram)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap -> 95

```