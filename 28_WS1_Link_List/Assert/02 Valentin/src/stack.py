
from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty:
            raise ValueError("Stack is empty")
        
        data = self.top.value
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty:
            raise ValueError("Stack is empty")
        return self.top.value

    @property
    def count(self):
        return self.size

    @property
    def is_empty(self):
        return self.size == 0
