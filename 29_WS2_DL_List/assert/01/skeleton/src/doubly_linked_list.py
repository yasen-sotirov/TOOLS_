from src.linked_list_node import LinkedListNode

# Finish the DoublyLinkedList class by providing the following functionality:
# - `add_first(value)` - adds an element to the head of the list
# - `add_last(value)` - adds an element to the tail of the list
# - `remove_first()` - removes the first node and returns its value
# - `remove_last()` - removes the last node and returns its value
# - `insert_before(node, value)` - insert an element with the given value before the given node
# - `insert_after(node, value)` - insert an element with the given value after the given node
# - `find(val)` - returns the first node that has the given value or null if no such value exists
# - `values()` - returns all values as a tuple
# - `head` - reference to the head node
# - `tail` - reference to the tail node
# - `count` - returns the number of nodes

class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        _new_node = LinkedListNode(value)
        if self._count > 0:
            _new_node.next = self._head
            self._head.prev, self._head = _new_node, _new_node
        else:
            self._head = self._tail = _new_node
        self._count +=1

    def add_last(self, value):
        _new_node = LinkedListNode(value)
        if self._count > 0:
            _new_node.prev = self._tail
            self._tail.next, self._tail = _new_node, _new_node
        else:
            self._head = self._tail = _new_node
        self._count +=1

    def insert_after(self, node, value):
        self._empty_list_error()
        if node == self._tail:
            self._insert_after_tail(value)
        else:
            current = self._find_node(node, True)
            if current:
                _new_node = LinkedListNode(value)
                _new_node.next = current.next
                _new_node.prev = current
                current.next.prev, current.next = _new_node, _new_node
                self._count += 1

    def insert_before(self, node, value):
        self._empty_list_error()
        if node == self._head:
            self._insert_before_head(value)
        else:
            current = self._find_node(node, True)
            if current:
                _new_node = LinkedListNode(value)
                _new_node.next = current
                _new_node.prev = current.prev
                current.prev.next, current.prev = _new_node, _new_node
                self._count += 1

    def remove_first(self):
        self._empty_list_error()
        if self._count > 1:
            output = self._head.value
            self._head = self._head.next
        else: # == 1
            output = self._head.value
            self._head = self._tail = None
        self._count -= 1
        return output

    def remove_last(self):
        self._empty_list_error()
        if self._count > 1:
            output = self._tail.value
            self._tail = self._tail.prev
        else: # == 1
            output = self._tail.value
            self._head = self._tail = None
        self._count -= 1
        return output


    def find(self, value):
        current = self._head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def values(self):
        output = []
        current = self._head
        while current:
            output.append(current.value)
            current = current.next
        return tuple(output)

    def _insert_before_head(self, value):
        self._empty_list_error()
        self.add_first(value)

    def _insert_after_tail(self, value):
        self._empty_list_error()
        self.add_last(value)

    def _empty_list_error(self):
        if self._count == 0:
            raise ValueError('DL-List is empty')
        
    def _find_node(self, node, skip_head = False):
        current = self._head if not skip_head else self._head.next
        while current:
            if current == node:
                return current
            current = current.next
        return None