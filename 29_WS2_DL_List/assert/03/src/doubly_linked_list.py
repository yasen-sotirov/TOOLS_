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
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._count += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def insert_after(self, node, value):
        if node is None:
            raise ValueError("Node cannot be None")

        new_node = LinkedListNode(value)
        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node
        node.next = new_node

        if node == self._tail:
            self._tail = new_node
        self._count += 1

    def insert_before(self, node, value):
        if node is None:
            raise ValueError("Node cannot be None")

        new_node = LinkedListNode(value)
        new_node.prev = node.prev
        new_node.next = node

        if node.prev:
            node.prev.next = new_node
        node.prev = new_node

        if node == self._head:
            self._head = new_node
        self._count += 1

    def remove_first(self):
        if self._head is None:
            raise ValueError("List is empty")

        removed_value = self._head.value
        if self._head == self._tail:
            self._tail = None
            self._head = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._count -= 1
        return removed_value

    def remove_last(self):
        if self._tail is None:
            raise ValueError("List is empty")

        removed_value = self._tail.value
        if self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._count -= 1
        return removed_value

    def find(self, value):
        current = self._head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    def values(self):
        node_values = []
        current = self._head
        while current:
            node_values.append(current.value)
            current = current.next
        return tuple(node_values)

    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self._head

        if self._head:
            self._head.prev = new_node
        self._head = new_node

        if self._tail is None:
            self._tail = new_node
        self._count += 1

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        new_node.prev = self._tail

        if self._tail:
            self._tail.next = new_node
        self._tail = new_node

        if self._head is None:
            self._head = new_node
        self._count += 1
