
from src.linked_list_node import LinkedListNode


class CustomQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    
    def dequeue(self):
        if self.front is None:
            raise ValueError("Queue is empty")
        
        data = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    @property
    def count(self):
        return self.size

    @property
    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.front is None:
            raise ValueError("Queue is empty")
        return self.front.value