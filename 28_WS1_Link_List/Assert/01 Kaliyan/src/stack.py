
from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self) -> None:
        
        self._top: LinkedListNode | None = None
        self._counter = 0

    @property
    def is_empty(self):
        return self._top == None
    
    @property
    def count(self):
        return self._counter
    
    def peek(self):
        if self.is_empty:
            raise ValueError
        
        return self._top.value
    
    def pop(self):
        if self.is_empty:
            raise ValueError
        
        current = self._top
        self._top = self._top.next
        self._counter -= 1
        
        return current.value

    def push(self, node):
        new_top = LinkedListNode(node)

        if self.is_empty:
            self._top = new_top
        else:
            new_top.next = self._top
            self._top = new_top

        self._counter += 1
        