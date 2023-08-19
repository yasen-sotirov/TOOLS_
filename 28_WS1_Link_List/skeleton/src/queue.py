
from src.linked_list_node import LinkedListNode


class CustomQueue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None


    def enqueue(self, element):
        new_node = LinkedListNode(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1


    def dequeue(self):
        if self.tail is None:
            raise ValueError
        else:
            el = self.head
            while el.next.next is not None:
                self.tail = el
                el = el.next

            self.count -= 1
            self.tail.next = None
            return self.tail.value


    def peek(self):
        if self.head is None:
            raise ValueError
        return self.head.value


    def count(self):
        return self.count


    @property
    def is_empty(self):
        return self.count == 0


