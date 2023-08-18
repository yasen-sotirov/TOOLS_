class Stack:
    def __init__(self):
        self._items = []

    def push(self, val):
        self._items.append(val)

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty')

        return self._items.pop()

    def peek(self):
        if self.is_empty:
            raise ValueError('Stack is empty')

        return self._items[-1]

    @property
    def is_empty(self):
        return len(self._items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

while not stack.is_empty:
    print(stack.peek())
    print(stack.pop())
