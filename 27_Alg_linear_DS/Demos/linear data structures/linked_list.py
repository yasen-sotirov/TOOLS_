from typing import TypeVar, Generic
from node import Node

# advanced type hinting, no relation to linked list
T = TypeVar('T')


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self._head: Node[T] | None = None

    def add_first(self, value: T) -> None:
        node = Node(value)
        node.next = self._head
        self._head = node

    def remove_first(self) -> T:
        if self._head is None:
            raise ValueError('List is empty')

        val = self._head.value
        self._head = self._head.next

        return val

    def insert_after(self, node: Node[T], value: T):
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def remove_after(self, node: Node[T]) -> None:
        if node.next is not None:
            node.next = node.next.next

    def find(self, value: T) -> Node[T] | None:
        ref = self._head
        while ref is not None:
            if value == ref.value:
                return ref

            ref = ref.next

        return None

    def get_values(self) -> list[T]:
        values = []
        ref = self._head
        while ref is not None:
            values.append(ref.value)
            ref = ref.next

        return values


## int-typed LinkedList
nums: LinkedList[int] = LinkedList()

nums.add_first(3)
nums.add_first(2)
nums.add_first(1)

nums.remove_after(nums.find(1))

for value in nums.get_values():
    print(value)

## string-typed LinkedList
foods: LinkedList[str] = LinkedList()

foods.add_first('coffee')
foods.add_first('banana')
foods.add_first('apple')

print(foods.find('coffee').value)
