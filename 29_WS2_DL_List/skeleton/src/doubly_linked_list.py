from src.linked_list_node import LinkedListNode

# isinstanse


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
        if self.head is None:
            self._head = new_node
            self._tail = new_node
        else:
            old_head = self.head
            self._head = new_node
            new_node.next = old_head
            old_head.prev = new_node
        self._count += 1



    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self.head is not None:
            old_tail = self.tail
            self._tail = new_node
            old_tail.next = self.tail
            self.tail.prev = old_tail
        else:
            self._head = new_node
            self._tail = new_node
        self._count += 1



    def insert_after(self, node, value):
        if self.count == 0:
            raise ValueError

        temp_head = self.head
        temp_tail = self.tail
        old_count = self.count

        if  self.tail.value == value:
            temp_tail.next = node
            node.prev = temp_tail
            self._tail = node

        while temp_head.next is not None:
            if temp_head.value == value:
                node.next = temp_head.next
                temp_head.next = node
                node.prev = temp_head
                self._tail = node
                self._count += 1
            temp_head = temp_head.next

        if self.count == old_count:
            return f"element not found"
        self._count += 1


    def insert_before(self, node, value):
        if self.count == 0:
            raise ValueError

        temp_head = self.head
        while temp_head.next is not None:

            if self.head.value == value:
                self._head = node
                self.head.next = temp_head
                temp_head.prev = self.head

            prev_temp_head = temp_head

            if temp_head.value == value:
                prev_temp_head.next = node
                node.prev = prev_temp_head
                node.next = temp_head
                temp_head.prev = node
            temp_head = temp_head.next
        self._count += 1



    def remove_first(self):
        if self.head is None:
            raise ValueError

        if self.count == 1:
            self._head = None
            self._tail = None
        else:
            self._head = self.head.next
            self._head.prev = None
        self._count -= 1



    def remove_last(self):
        if self.head is None:
            raise ValueError

        elif self.count > 1:
            self._tail = self.tail.prev
            self.tail.next = None

        elif self.count == 1:
            self._head = None
            self._tail = None
        self._count -= 1



    def find(self, value):
        if self.head is None:
            return None
        node = self.head
        if self.tail.value == value:
            return self.tail.value
        while node.next is not None:
            if value == node.value:
                return node.value
            node = node.next



    def values(self):
        if self.count == 0:
            return tuple()
        lst = []
        while self.head.next is not None:
            lst.append(self.head.value)
            self._head = self.head.next
        lst.append(self.head.value)
        return tuple(lst)



    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self._head = new_node
            self._tail = new_node
        else:
            old_head = self.head
            self._head = new_node
            new_node.next = old_head
            old_head.prev = new_node
        self._count += 1




    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        if self.tail is None:
            raise ValueError
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self._tail = new_node
            self._count += 1
