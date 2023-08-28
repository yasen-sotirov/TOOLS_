"""
Shuffle

Your task is to implement a brand new algorithm for shuffling numbers. The numbers will be from 1 to N.
You will receive K numbers, which will be the ones you will shuffle following the rules below:
    If the number to be shuffled is even -> move it after the number with value = numberToBeShuffled / 2
    (i.e. if you need to shuffle 4 you need to move it after 2).
    If the number to be shuffled is odd -> move it after the number with value = numberToBeShuffled * 2
    (i.e. if you need to shuffle 3 you need to move it after 6).
    If numberToBeShuffled * 2 > N move it after the number with value N.
    If the number to be shuffled should be moved after the same number -> do nothing.

Input

    Read from the standard input
    On the first line, find the number N and K
        N - numbers will be from 1 to N
        K - the count of numbers which will be found on the next line of the input
    On the next line there will be K numbers
    The numbers to be shuffled (all in range from 1 to N)

Output
    Print on the standard output
    On a single line, print the shuffled numbers

Constraints
    1 <= N <= 100
    1 <= K <= 400 000

    Sample tests
Input
7 4
1 5 4 7

Output
2 4 1 3 6 7 5

Explanation

    You have the numbers 1 2 3 4 5 6 7. First you need to move 1 which is odd,
    so we move it after 1 * 2 = 2 -> 2 1 3 4 5 6 7
    Move 5 which is odd, so we should move it after 5 * 2 = 10,
    but it is greater than 7, so we move it after 7 -> 2 1 3 4 6 7 5
    Move 4 which is even, so we move it after 4 / 2 = 2 -> 2 4 1 3 6 7 5
    Move 7 which is odd, so we should move it after 7 * 2 = 14,
    but it is greater than 7, so we need to move it after 7, which is the number to be moved, so we do nothing -> 2 4 1 3 6 7 5

Input
10 5
10 2 1 6 8

Output
2 1 3 6 4 8 5 10 7 9

Input
5 5
1 2 1 2 5

Output
1 2 3 4 5
"""


class Node:
    def __init__(self, node_value):
        self.node_value = node_value
        self.next: Node = None
        self.prev: Node = None


class Order:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None


    def add_after(self, aft_node, moved_node):
        self.remove_node(moved_node)
        if aft_node == self.tail:
            moved_node.prev = self.tail
            self.tail.next = moved_node
            self.tail = moved_node
        elif after_node == self.head:
            next_node = aft_node.next
            moved_node.next = next_node
            next_node.prev = moved_node
            moved_node.prev = self.head
            self.head.next = moved_node
        else:
            next_node = aft_node.next
            moved_node.next = next_node
            next_node.prev = moved_node
            moved_node.prev = after_node
            aft_node.next = moved_node



    def remove_node(self, remove_node):
        if remove_node == self.head:
            nex_node = remove_node.next
            self.head = nex_node
            self.head.prev = None
            remove_node.prev = None
            remove_node.next = None
        elif remove_node == sequence.tail:
            p_node = remove_node.prev
            p_node.next = None
            self.tail = p_node
            remove_node.prev = None
            remove_node.next = None
        else:
            p_node = remove_node.prev
            next_node = remove_node.next
            p_node.next = next_node
            next_node.prev = p_node
            remove_node.prev = None
            remove_node.next = None


num_range, move = [int(el) for el in input().split()]
nums_to_move = [int(el) for el in input().split()]

sequence = Order()
first_order = {}

prev_node = None
for current_num in range(1, num_range + 1):
    new_node = Node(current_num)
    first_order[current_num] = new_node

    if sequence.head is None:
        sequence.head = new_node
        sequence.tail = new_node
    else:
        prev_node.next = new_node
        new_node.prev = prev_node
        sequence.tail = new_node
    prev_node = new_node


for num in nums_to_move:
    if num % 2 == 0:
        after_num = num / 2
    else:
        after_num = num * 2

    if after_num > num_range:
        after_num = num_range
    if num == after_num:
        break

    after_node = first_order[after_num]
    move_node = first_order[num]
    sequence.add_after(after_node, move_node)

node = sequence.head
while node:
    print(node.node_value, end=" ")
    node = node.next










