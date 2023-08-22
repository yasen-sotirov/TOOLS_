from src.linked_list_node import LinkedListNode

class CustomQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self.count = 0

    def enqueue(self, value):
        new_node = LinkedListNode(value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty')
        value = self._head.value
        self._head = self._head.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty')
        return self._head.value

    @property
    def is_empty(self):
        return self._head is None
