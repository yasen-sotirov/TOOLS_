
from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.count = 0
        self.head = None
        self.start_el = None


    def push(self, element):
        new_node = LinkedListNode(element)
        if self.head is None:
            self.head = new_node
            self.start_el = new_node
        else:
            self.head.next = new_node
            self.head = new_node
        self.count += 1


    def pop(self):
        if self.head is None:
            raise ValueError
        else:
            current_el = self.start_el
            while current_el.next == self.head:
                self.head = current_el
                self.head.next = None

        self.count -= 1
        return self.head.value


    def peek(self):
        if self.head is None:
            raise ValueError
        return self.head.value


    def count(self):
        return self.count


    @property
    def is_empty(self):
        return self.count == 0

