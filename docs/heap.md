# Heap

## API Details

| Usage                                       | Function                | Time    | Space |
|---------------------------------------------|-------------------------|---------|-------|
| Build a max heap from an array              | Heap(arr, HeapType.MAX) | O(N)    | O(1)  |
| Build a min heap from an array              | Heap(arr, HeapType.MIN) | O(N)    | O(1)  |
| Peek an element from the heap               | peek()                  | O(1)    | O(1)  |
| Insert an element into heap(`heapify_up`)   | insert(element)         | O(logN) | O(1)  |
| Remove an element into heap(`heapify_down`) | remove()                | O(logN) | O(1)  |




## Example

```python
#!/usr/bin/env python3
# description: demo heap
# author: greyshell

from libozone import Heap, HeapType


class Student:
    """helper class"""

    def __init__(self, name: str, score: int):
        self.name = name
        self.key = score  # determines the priority

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key


if __name__ == '__main__':
    # example of min heap
    arr = [5, 9, 2]
    hmin = Heap(arr)  # create a min heap

    if hmin:  # check for emptiness before peek
        print(hmin.peek())  # peek the min item from the heap -> 2
    else:
        print('no heap elements')

    hmin.insert(1)  # insert an item into the heap

    if hmin:  # check emptiness before remove
        print(hmin.remove())  # remove an item from the heap -> 1
    else:
        print('no heap elements')

    print(len(hmin))  # print the length of the heap -> 3
    print(hmin)  # print all items from the heap -> [2, 9, 5]
    print("")

    # example of max heap
    arr = [5, 9, 2]
    hmax = Heap(arr, heap_type=HeapType.MAX)  # create a max heap

    if hmax:  # check for emptiness before peek
        print(hmax.peek())  # peek the max item from the heap -> 9
    else:
        print('no heap elements')

    hmax.insert(10)  # insert an item into the heap

    if hmax:  # check for emptiness before remove
        print(hmax.remove())  # remove an item from the heap -> 10
    else:
        print('no heap elements')

    print("")

    # example of a max-heap of Student objects where priority is determined by score
    alice = Student(name="alice", score=80)
    bob = Student("bob", 90)
    malory = Student("malory", 75)
    tom = Student("tom", 85)

    arr = [alice, bob, malory, tom]
    student_heap = Heap(arr, HeapType.MAX)

    if student_heap:  # check emptiness before peek
        student_obj = student_heap.peek()
        print(f"student: {student_obj.name}, score: {student_obj.key}")  # student: bob, score: 90
    else:
        print('no heap elements')

    ram = Student("ram", 95)  # creating the student object
    student_heap.insert(ram)  # insert the student object in to heap

    if student_heap:  # check emptiness before remove
        student_obj = student_heap.remove()
        print(f"student: {student_obj.name}, score: {student_obj.key}")  # student: ram, score: 95
    else:
        print('no heap elements')

    carol = Student("carol", 90)  # creating a student object with same score as bob
    student_heap.insert(carol)  # insert the student object into heap

    if student_heap:  # check emptiness before peek
        student_obj = student_heap.peek()
        print(f"student: {student_obj.name}, score: {student_obj.key}")  # student: bob, score: 90
    else:
        print('no heap elements')

```