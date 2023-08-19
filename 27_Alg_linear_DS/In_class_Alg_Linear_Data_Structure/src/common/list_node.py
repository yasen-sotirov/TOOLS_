class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next: ListNode = next


class LinkedList:
    def __init__(self, nodes_list=None):
        self.head = None
        self.tail = None
        # проверява дали листа е празен
        if nodes_list is not None:
            #  създава първия възел  с първия елемент на списъка
            current_node = ListNode(value=nodes_list.pop(0))
            # закача главата към първия възел
            self.head = current_node
            # итерира през списъка и навързва останалите елементи
            for el in nodes_list:
                # създава нова инстанция и връзва текущия възел към нея
                current_node.next = ListNode(value=el)
                # настоящ е вече следващият елемент
                current_node = current_node.next
        self.tail = current_node