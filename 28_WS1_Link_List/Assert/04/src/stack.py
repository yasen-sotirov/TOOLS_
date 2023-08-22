
from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.head = None
        self.size = 0

    @property
    def count(self):
        counter = 0
        current_el = self.head

        while current_el: #Докато не е None
            counter += 1 # Означава,че има counter и го добавя
            current_el = current_el.next #1 > 2 1 става на 2 става на 3 и така обикаля
        return counter
    
    @property
    def is_empty(self):
        return self.size == 0

    def push(self,data):
        self.head = LinkedListNode(data , self.head)
        self.size += 1
    
    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty')
        result = self.head.value
        self.head = self.head.next
        self.size -= 1
        
        return result
    
    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty')
        return self.head.value