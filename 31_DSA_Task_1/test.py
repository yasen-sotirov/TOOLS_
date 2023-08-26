number_of_students, number_of_seat_changes = [int(x) for x in input().split()]
start_order = {}
for idx, name in enumerate(input().split()):
    start_order[name] = idx

list_of_changes = {}
for _ in range(number_of_seat_changes):
    new_change = input().split()
    list_of_changes[new_change[0]] = new_change[1]

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self._next = next
        self._prev = prev


class NewLinkedList:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0

    def append(self, element_value: str):
        new_node = Node(element_value)
        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail
            self._tail = new_node

        self._size += 1

    def remove(self, founded_node):
        if founded_node._prev == None:
            self._head = founded_node._next
            founded_node._next._prev = None
            founded_node._next = None

        elif founded_node._next == None:
            self._tail = founded_node._prev
            founded_node._prev._next = None
            founded_node._prev = None

        else:
            founded_node._next._prev = founded_node._prev
            founded_node._prev._next = founded_node._next
            founded_node._next = None
            founded_node._prev = None

        self._size -= 1

    def insert_before(self, new_node, existing_node):
        if existing_node._prev == None:
            existing_node._prev = new_node
            new_node._next = existing_node
            self._head = new_node

        else:
            existing_node._prev._next = new_node
            new_node._prev = existing_node._prev
            existing_node._prev = new_node
            new_node._next = existing_node

        self._size += 1

    def change(self, moving_el_node, main_node):
        self.remove(moving_el_node)
        self.insert_before(moving_el_node, main_node)

    def get_order(self):
        ref = self._head
        res = []
        while ref:
            res.append(ref.value)
            ref = ref._next

        return ' '.join(map(str, res))

    def find(self, element_value):
        ref = self._head
        while ref:
            if ref.value == element_value:
                return ref
            ref = ref._next


        return False


double_linked = NewLinkedList()
for name, idx in start_order.items():
    double_linked.append(name)

for moving_el, main in list_of_changes.items():
    moving_el_node = double_linked.find(moving_el)
    main_node = double_linked.find(main)
    double_linked.change(moving_el_node, main_node)


print(double_linked.get_order())




