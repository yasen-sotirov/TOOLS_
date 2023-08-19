# 2 стъпка - бързо създаване на линкове

class LinkedList:
    def __init__(self, nodes_list=None):
        self.head = None
        self.tail = None
        # проверява дали листа е празен
        if nodes_list is not None:
            #  създава първия възел  с първия елемент на списъка
            current_node = Node(value=nodes_list.pop(0))
            # закача главата към първия възел
            self.head = current_node
            # итерира през списъка и навързва останалите елементи
            for el in nodes_list:
                # създава нова инстанция и връзва текущия възел към нея
                current_node.next = Node(value=el)
                # настоящ е вече следващият елемент
                current_node = current_node.next
        self.tail = current_node


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


llist = LinkedList(["a", "b", "c", "d", "e", "f"])

print(llist.head)
print(llist.tail)