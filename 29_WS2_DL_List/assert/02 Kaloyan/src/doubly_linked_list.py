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
        if not self._head:
            new_node = LinkedListNode(value)
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_before_head(value)

        self._count += 1

    def add_last(self, value):
        if not self._tail:
            new_node = LinkedListNode(value)
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_after_tail(value)

        self._count += 1


    def insert_after(self, node: LinkedListNode, value: int):
        if not node:
            raise ValueError('Not found')
        
        found_node = self.find(node.value)
        
        if found_node.next:
            new_node = LinkedListNode(value)
            new_node.next = found_node.next
            new_node.prev = found_node
            new_node.next.prev = new_node
            found_node.next = new_node
        else:
            self._insert_after_tail(value)

        self._count += 1

    def insert_before(self, node: LinkedListNode, value: int):
        if not node:
            raise ValueError('Not found')
        
        found_node = self.find(node.value)

        if found_node.prev:
            new_node = LinkedListNode(value)
            new_node.next = found_node
            new_node.prev = found_node.prev
            found_node.prev.next = new_node
            found_node.prev = new_node
        else:
            self._insert_before_head(value)

        self._count += 1

    def remove_first(self):
        if self._count == 0:
            raise ValueError('List is empty!')
        
        ref = self._head.value
        self._head = self._head.next
        self._count -= 1
        return ref

    def remove_last(self):
        if self._count == 0:
            raise ValueError('List is empty!')

        ref = self._tail.value
        self._tail = self._tail.prev
        self._count -= 1
        return ref

    def find(self, value):
        if self._count == 0:
            return

        ref = self._head
        while ref:
            if ref.value == value:
                return ref
            ref = ref.next
        return

    def values(self):
        if self._count == 0:
            return ()
        
        result = []
        ref = self._head
        while ref:
            result.append(ref.value)
            ref = ref.next
    
        return tuple(result)


    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node
