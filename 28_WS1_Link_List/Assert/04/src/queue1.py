from src.linked_list_node import LinkedListNode


class CustomQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise ValueError('Queue is empty!')
        data = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    @property
    def count(self):
        counter = 0
        current_el = self.head

        while current_el:
            counter += 1 
            current_el = current_el.next
        return counter
    
    @property
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty')
        return self.head.value
