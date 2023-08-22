from src.linked_list_node import LinkedListNode

class CustomStack:
    def __init__(self):
        self._top = None
        self.count = 0

    def push(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self._top
        self._top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty')
        value = self._top.value
        self._top = self._top.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty')
        return self._top.value

    @property
    def is_empty(self):
        return self._top is None
