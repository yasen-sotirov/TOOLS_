"DOUBLY LINKED LIST"    # свързан списък

'''
Линейна структура от данни базирана на референции.
Елементите не са разположени последователно, където има място в паметта. 
Следователно няма начин да се направи ефективна индексация.
Може да бъде направена, но тя ще работи с линейна сложност, което не е оптимално.

два основни типа:
    Единично свързани   = две property-a: value & next
    Двойно свързани     = три property-a: value, prev, next '''

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None  # референция
        self.prev: Node = None




class DoublyLinkedList:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None
        self._count = 0

    ""
    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail


    def append_node(self, new_node: Node):
        if not self._head:
            self._head = new_node
            self._tail = new_node

        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

        self._count += 1


    "СЛАГА В НАЧАЛОТО"
    def add_first(self, value):
        if not self._head:
            new_node = Node(value)
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_before_head(value)

        self._count += 1


    def add_last(self, value):
        if not self._tail:
            new_node = Node(value)
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_after_tail(value)

        self._count += 1


    def insert_after(self, node: Node, value: int):
        if not node:
            raise ValueError('Not found')

        found_node = self.find(node.value)

        if found_node.next:
            new_node = Node(value)
            new_node.next = found_node.next
            new_node.prev = found_node
            new_node.next.prev = new_node
            found_node.next = new_node
        else:
            self._insert_after_tail(value)

        self._count += 1


    def insert_before(self, node: Node, value: int):
        if not node:
            raise ValueError('Not found')

        found_node = self.find(node.value)

        if found_node.prev:
            new_node = Node(value)
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
        result = []
        ref = self._head
        while ref:
            result.append(ref.value)
            ref = ref.next

        return tuple(result)


    def _insert_before_head(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node


    def _insert_after_tail(self, value):
        new_node = Node(value)
        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node


    def display(self):      # накрая ще покаже None, което е правилно
        current_node = self._head
        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.next


"СЪЗДАВАНЕ НА ЛИСТ И НОДОВЕ"
dll = DoublyLinkedList()
node_list = []

node_1 = Node(1)
node_list.append(node_1)
node_2 = Node(2)
node_list.append(node_2)
node_3 = Node(3)
node_list.append(node_3)
node_4 = Node(4)
node_list.append(node_4)

for el in node_list:
    print(el.value)
    print('-----')


"ЗАКАЧАНЕ КЪМ ЛИСТА"
for el in node_list:
    dll.append_node(el)
print(dll.display())


"ПРЕМАХВАНЕ НА ПЪРВИЯ"
dll.remove_first()
print(dll.display())


"НАМИРАНЕ НА НОД"
node = dll.find(3)
print(node.value)
