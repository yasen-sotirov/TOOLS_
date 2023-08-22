from src.linked_list_node import LinkedListNode


class CustomQueue:

    def __init__(self) -> None:
        self._head: LinkedListNode | None = None
        self._tail: LinkedListNode | None = None
        self._counter = 0

    @property
    def count(self):
        return self._counter

    @property
    def is_empty(self):
        return self._tail == None
    
    def dequeue(self):
        if self.is_empty:
            raise ValueError
        
        current_head = self._head
        self._head = self._head.next

        self._counter -= 1
        return current_head.value

    def enqueue(self, node):
        new_node = LinkedListNode(node)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
            
        else:
            self._tail.next = new_node
            self._tail = new_node
      
        self._counter += 1

    def peek(self):
        if self.is_empty:
            raise ValueError
        return self._head.value
    