from src.common.list_node import ListNode
# from src.common.stack import Stack

# # task 1
#
# def find_middle_of_list(head: ListNode):
#     raise NotImplementedError()
#
# # task 2
#
def merge_sorted_lists(h1: ListNode, h2: ListNode):
    merged = ListNode(None)
    current = merged




# task 3
#
# def reverse_list(head: ListNode):
def reverse_list(head: ListNode):
    if head is None or head.next is None:
        return head
    a = None
    while head.next is not None:
        new_tail = head
        new_head = head.next
        head = new_head
        new_tail.next = a
        a = new_tail
    head.next = a

    return head





#
# # task 4
#
# def validate_parentheses(expr: str):
#     raise NotImplementedError()
#


# task 5
# sequence: 'abc#d'
# returns: 'abd'

# sequence: 'abcd##e##'
# returns: 'a'
# def backspace_char(sequence: str):
#     lst = []
#     for el in sequence:
#         if el == "#" and lst == []:
#             continue
#         elif el == "#":
#             lst.pop()
#         else:
#             lst.append(el)
#
#     return "".join(lst)

print(backspace_char("#abc#d"))













