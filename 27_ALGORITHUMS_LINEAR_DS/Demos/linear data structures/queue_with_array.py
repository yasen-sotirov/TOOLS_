class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, val):
        self._items.append(val)

    def dequeue(self):
        if self.is_empty:
            raise ValueError('Queue is empty')

        # WARNING: this is functionally correct, but has O(n) complexity,
        # which is not optimal for dequeue
        return self._items.pop(0)

    def peek(self):
        if self.is_empty:
            raise ValueError('Queue is empty')

        return self._items[0]

    @property
    def is_empty(self):
        return len(self._items) == 0


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

while not q.is_empty:
    print(q.peek())
    print(q.dequeue())
