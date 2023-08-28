from src.linked_list_node import LinkedListNode


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
        new_node = LinkedListNode(value)
        if not self.head:
            self._head = self._tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self._head = new_node
        self._count += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if not self.tail:
            self._head = self._tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self._tail = new_node
        self._count += 1

    def insert_after(self, node, value):
        if not node:
            raise ValueError("Node cannot be None.")
        new_node = LinkedListNode(value)
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if node == self.tail:
            self._tail = new_node
        self._count += 1

    def insert_before(self, node, value):
        if not node:
            raise ValueError("Node cannot be None.")
        new_node = LinkedListNode(value)
        new_node.prev = node.prev
        new_node.next = node
        if node.prev:
            node.prev.next = new_node
        node.prev = new_node
        if node == self.head:
            self._head = new_node
        self._count += 1

    def remove_first(self):
        if not self.head:
            raise ValueError("Empty list.")
        value = self.head.value
        if self.head == self.tail:
            self._head = self._tail = None
        else:
            self._head = self.head.next
            self.head.prev = None
        self._count -= 1
        return value

    def remove_last(self):
        if not self.tail:
            raise ValueError("Empty list")
        value = self.tail.value
        if self.head == self.tail:
            self._head = self._tail = None
        else:
            self._tail = self.tail.prev
            self.tail.next = None
        self._count -= 1
        return value

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def values(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return tuple(values)

    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._count += 1

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1
