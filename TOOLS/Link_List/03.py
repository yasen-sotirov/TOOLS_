# 3 добавяне на елементи

class LinkedList:
    def __init__(self, nodes_list=None):
        self.head = None
        self.tail = None
        # проверява дали листа е празен
        if nodes_list is not None:
            #  създава първия възел  с първия елемент на списъка
            current_node = Node(data=nodes_list.pop(0))
            # закача главата към първия възел
            self.head = current_node
            # итерира през списъка и навързва останалите елементи
            for el in nodes_list:
                # създава нова инстанция и връзва текущия възел към нея
                current_node.next = Node(data=el)
                # настоящ е вече следващият елемент
                current_node = current_node.next
        self.tail = current_node


    def add_first(self, node_to_add_first):
        node_to_add_first.next = self.head
        self.head = node_to_add_first

    # ако не знам къде е опашката
    def add_last_el(self, final_node):
        # проверява дали има елементи в списъка
        if self.head is None:
            # ако няма, връзва главата към новия елемент
            self.head = final_node
            self.tail = final_node
            # спира функцията
            return

        # вижда кой е първия елемент
        current_node = self.head
        # ако има други елементи в колекцията итерира през тях докато достигне последния ел
        while current_node.next is not None:
            # прехвърля се на следващия ел
            current_node = current_node.next
        # когато го достигне, насочва неговия next към последния ел
        current_node.next = final_node
        # казва на опашката кой е последния ел
        self.tail = final_node


    # добавя възел след възел с определено съдържание
    def add_after_node(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        # итерира през списъка
        current_node = self.head
        while current_node is not None:
            # намира търсеното value
            if current_node.data == target_node_data:
                # привързва новия елемент, към елемента след търсения ел
                new_node.next = current_node.next
                # привързва търсеният елемент към новия ел
                current_node.next = new_node
                return
            current_node = current_node.next
        raise Exception("Node with data '%s' not found" % target_node_data)



    def view_list(self):
        if self.head is None:
            raise Exception("List is empty")

        el = self.head
        print_list = []
        while el is not None:
            print_list.append(el)
            el = el.next
        return print_list



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data



# създава свързаният лист
llist = LinkedList(["a", "b", "c", "d", "e", "f"])
print(f"first el: {llist.head}")
print(f"last el: {llist.tail}")


# добавя елемент в началото
el_to_add_first = Node("0")
llist.add_first(el_to_add_first)
print(f"first el: {llist.head}")


# добавя ел в края
print()
print("добавям 'х'")
final_el = Node("x")
llist.add_last_el(final_el)
print(f"last added el: {llist.tail}")

# добавяме след определен възел
print()
print(f"добавяме след 'c'")
node_to_add_between = Node("c2")
llist.add_after_node("c", node_to_add_between)

print(llist.view_list())