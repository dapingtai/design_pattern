from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any, List

# Iterator
class LinkedListIterator(Iterator):
    def __init__(self, collection: LinkedList) -> None:
        self._collection = collection
        self._current = collection.head
        self._index = 0

    def __next__(self) -> Any:
        try:
            value = self._current.data
            self._current = self._current.next
            self._index += 1
            return value
        except AttributeError:
            raise StopIteration()

# Node for LinkedList
class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

# Concrete Collection (Iterable)
class LinkedList(Iterable):
    def __init__(self) -> None:
        self.head = None
        self._count = 0

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)

    def add(self, data: Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._count += 1

    def size(self) -> int:
        return self._count

def main():
    # Create collection
    linked_list = LinkedList()

    # Add elements
    linked_list.add("First")
    linked_list.add("Second")
    linked_list.add("Third")

    # Use for loop (implicit iterator)
    print("Iterating through linked list:")
    for item in linked_list:
        print(f"- {item}")

    # Use iterator explicitly
    print("\nUsing iterator explicitly:")
    iterator = iter(linked_list)
    try:
        while True:
            print(f"- {next(iterator)}")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()