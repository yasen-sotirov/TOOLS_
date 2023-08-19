"""LINKED LIST      изцяло нов вид

състоят се от Nodes, който съдържа две неща:
- data
- линк към следващия лист
- последния Node  сочи към None




random access - можем да скочим на всяко място в листа,
защото знаем индеса му
"""


"СЪЗДАВАНЕ НА LINK LIST"
# https://realpython.com/linked-lists-python/#:~:text=Each%20element%20of%20a%20linked,next%20node%20on%20the%20list.

# просто навръзване
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while nodes is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append(None)
        return "->".join(nodes)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value



llist = LinkedList()

first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
