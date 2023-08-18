from __future__ import annotations
from typing import TypeVar, Generic

# advanced type hinting, no relation to linked list
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T, next: Node[T] | None = None):
        self.value: T = value
        self.next = next
