from src.common.list_node import ListNode
from src.common.stack import Stack

# task 1


def find_middle_of_list(head: ListNode):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# task 2

def merge_sorted_lists(h1: ListNode, h2: ListNode):
    merged = ListNode(None)
    current = merged

    while h1 and h2:
        if h1.value < h2.value:
            current.next = ListNode(h1.value)
            h1 = h1.next
        else:
            current.next = ListNode(h2.value)
            h2 = h2.next

        current = current.next

    current.next = h1 if h1 else h2

    return merged.next


# task 3

def reverse_list(head: ListNode):
    prev = None

    while (head):
        temp_next = head.next

        head.next = prev
        prev = head
        head = temp_next

    return prev


# task 4

def validate_parentheses(expr: str):
    tracker = Stack()

    for ch in expr:
        if ch == '(':
            tracker.push(ch)
        elif ch == ')':
            if tracker.is_empty():
                return False
            else:
                tracker.pop()

    return tracker.is_empty()

# task 5


def backspace_char(sequence: str):
    chars = Stack()

    for ch in sequence:
        if ch == '#' and not chars.is_empty():
            chars.pop()
        elif ch != '#':
            chars.push(ch)

    output = ''
    while not chars.is_empty():
        output = f'{chars.pop()}{output}'

    return output
