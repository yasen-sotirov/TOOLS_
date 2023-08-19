from src.common.list_node import ListNode
from src.common.list_node import LinkedList
from src.common.stack import Stack


"""
===== task 1   Middle of the Linked List
The function takes the head of a singly linked list and
returns a new list which starts at the middle of the original one:
head: 1 -> 2 -> 3 -> None
returns: 2 -> 3 -> None

head: 1 -> 2 -> 3 -> 4 -> None
returns: 3 -> 4 -> None
"""
# def find_middle_of_list(head: ListNode):
#     slow = head
#     fast = head
#
#     while fast.next and fast:
#         slow = slow.next
#         fast = fast.next.next
#     return slow.value




# ===== task 2
#
# def merge_sorted_lists(h1: ListNode, h2: ListNode):
#     merged = ListNode(None)
#     current = merged




# ===== task 3
#
def reverse_list(head: ListNode):
    if head is None or head.next is None:
        return head
    el = None
    while head.next is not None:
        new_tail = head
        new_head = head.next
        head = new_head
        new_tail.next = el
        el = new_tail
    head.next = el

    return head






"""# ===== task 4
The function takes the heads of the sorted linked lists (h1, h2) and returns the
head of a new sorted linked list, that is the merge of the other two:
h1: 1 -> 2 -> 3 -> None
h2: 1 -> 4 -> None
returns: 1 -> 1 -> 2 -> 3 -> 4 -> None"""

# def validate_parentheses(expr: str):
#     pass



"""
===== task 5
sequence: 'abc#d'
returns: 'abd'

sequence: 'abcd##e##'
returns: 'a'
"""
# def backspace_char(sequence: str):
#     lst = []
#     for el in sequence:
#         if el == "#" and lst == []:
#             continue    # започва нов цикъл
#         elif el == "#":
#             lst.pop()
#         else:
#             lst.append(el)
#
#     return "".join(lst)
#
# print(backspace_char("#abc#d"))




llist = LinkedList(["a", "b", "c", "d", "e", "f"])
find_middle_of_list(llist)




