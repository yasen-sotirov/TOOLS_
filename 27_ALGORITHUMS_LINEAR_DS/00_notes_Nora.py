"""  АЛГОРИТМИ И ЛИНЕАРНИ ДАТА СТРУКТУРИ

# https://www.educative.io/courses/mastering-data-structures-and-sorting-algorithms-in-javascript/3j6xyKXNBqx


О(1)    ->    constant  има само една операция в алгоритъма
при 5 операции при ато елемента и 10к елемента пак имаме само 5 операции

броят операции не се определя от входящите данни




О(log n)    -> logarithmic  логаритъм при основа 2 от n  е степента на която 2 трябва да бъде сложено за да се плоучи
знаем информацията къде горе долу се намира в списъка

10 операции




О(n)    ->  linear    пример list броя на елементите определя сложността
5 * 1k = 5k операции
5 * 10к = 50к операции
минаваме през всеки елемент


O(n^2) ->   quadratic

5 * 1к * 1к = 1 000 000 операции
5 * 10к * 10к = 1 000 000 000 операции




                            n=1 000     n= 1 000k

O(1)  constant              3           3
a, b, c = input
sum = a + b + c



O(log n)                    10          20

O(n) linear                 1 000        1 000k



O(n^2) quadratic            1 000k       1 000 000k
for a in range(x)
    for b in range(y)
        sum += (a*b)

"""


"""
ЛИНЕЙНИ СТРУКТУРИ ОТ ДАННИ 
поредица (линия) от подредени данни, няма разклонения



Abstract data type - GPT?




list (dynamic)  данните са последователно подредени в паметта
позволява рамдом достъп по индекс
когато добавим нов елемент, ако следващите съседни клетки са заети, 
python премества целия списък на ново място където има поне 
1,5-2 пъти дължината на списъка място


Stack (link list) еднопосочно и двупосочно свързан
pointer-based 
съдържа референция към каквото съдържа и какво следва след него
няма значение къде са сложени в паметта

началото е Head, края е tail
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
print()


node = Node(1)
node.next = Node(2)
node.next.next = Node(5)

def traverse(head):
    while head:
        print(head.value)
        head = head.next


traverse(node)

