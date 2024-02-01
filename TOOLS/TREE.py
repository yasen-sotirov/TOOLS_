"TREES"   # ДЪРВЕТА
# Абстрактна структура от данни, която свързват елементи подобно на
# свързаните списъци, но по иеархичен, а не по линеен начин



class Category:
    def __init__(self, name: str, child):
        self.name = name
        self.child = child


categories = Category("Categories", [
                Category("PC and laptops", [
                    Category("Desktops", []),
                    Category("Laptops", []),
                    Category("Peripheral", [
                        Category("Mouse", [
                            Category("Bluetooth", []),
                            Category("With cabal", [])]),
                        Category("Keyboard", []),
                        Category("Other",[])])]),
                Category("TV's", [
                    Category("LCD", []),
                    Category("OLED", [])])])



"ОБХОЖДАНЕ РЕКУРСИВНО  DFS"  # Preorder
# def dfs(tree):
#     print(tree.name)
#     for child in tree.child:
#         dfs(child)
#
# dfs(categories)



"ОБХОЖДАНЕ РЕКУРСИВНО  BFS"
# def bfs(root):
#     q = Queue()
#     q.put(root)
#
#     while not q.empty():
#         next = q.get()
#         print(next.value)
#         for child in next.children:
#             q.put(child)
#
# bfs(categories)





""" 
TREE TRAVERSAL

Depth-First Search: 
    - Избира се един път и се следва възможно най дълбоко - до листата.
    - имплементира се с рекурсия или стек
    - видове DFS: 

    Preorder       Inorder        Postorder

       1              2               3
     /              /   \              \     
    2 –– 3         1     3          1 ––2


Breadth-First Search or Level Order Traversal:   
    - изследва всички деца на един връх и тогава слиза на долно ниво
    - имплементира се с Queue
    - при търсене на най-кратък път между два върха



БАЛАНСИРАНО ДЪРВО   (нарично още AVL дърво)
    Разликата между височините на лявото и дясното поддърво за всеки 
    възел е известна като фактор на баланс на възела.

    При тях разликите между височините на ляво и дясно поддървета 
    за всеки възел са по-малки или равни на 1.


TYPE HINTING
    from __future__ import annotations
    импортирам^ ако искам type hinting при създаване на класа child: list[Category] """




" ===== ВИЗУАЛИЗАЦИЯ ===== "
"--------------------------"

"ОБХОЖДАНЕ ЗА ВИЗУАЛИЗАЦИЯ ИТЕРАТИВНО"
# def visual_iter(tree: Category):
#     # тук ще трупаме подкатегориите
#     stack = [(tree, 0)]
#
#     while stack:
#         # вадим последния влязъл
#         curr_category, indent = stack.pop()
#         print(" " * indent, curr_category.name)
#
#         # прилагаме reversed иначе обръща подредбата
#         for child in reversed(curr_category.child):
#             # добавя децата към стека
#             stack.append((child, indent + 2))
#
# visual_iter(categories)


"ОБХОЖДАНЕ ЗА ВИЗУАЛИЗАЦИЯ РЕКУРСИВНО С ИДЕНТАЦИЯ  DFS"
# def visual_rec(category: Category, indent=0):
#     print(" " * indent, category.name)
#
#     for child in category.child:
#         visual_rec(child, indent + 2)
#
# visual_rec(categories)





" ===== BINARY SEARCH TREE ===== "
"--------------------------------"
from queue import Queue

class Bi_Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bi_tree = Bi_Tree(7,
            left=Bi_Tree(4,
            left=Bi_Tree(2),
                right=Bi_Tree(5,
                    right=Bi_Tree(6))),
            right=Bi_Tree(11,
                left=Bi_Tree(8),
                right=Bi_Tree(14,
                    right=Bi_Tree(18))))


"DFS PREORDER RECURSIVE"
# def dfs_preorder(root):
#     if root is None:
#         return
#
#     print(root.value)           # връх
#     dfs_preorder(root.left)     # ляво
#     dfs_preorder(root.right)    # дясно
#
# dfs_preorder(bi_tree)



"DFS INORDER RECURSIVE"
# def dfs_inorder(root):
#     if root is None:
#         return
#
#     dfs_inorder(root.left)    # ляво
#     print(root.value)         # връх
#     dfs_inorder(root.right)   # дясно
#
# dfs_inorder(bi_tree)



"DFS POSTORDER RECURSIVE"
# def dfs_postorder(root):
#     if root is None:
#         return
#
#     dfs_postorder(root.left)    # ляво
#     dfs_postorder(root.right)   # дясно
#     print(root.value)           # връх
#
# dfs_postorder(bi_tree)



"BFS TRAVERSAL   ITERATIVELY"
# def bfs_traversal(root):
#     q = Queue()
#     q.put(root)
#
#     while not q.empty():
#         next = q.get()
#         print(next.value)
#         if next.left is not None:
#             q.put(next.left)
#         if next.right is not None:
#             q.put(next.right)
#
# bfs_traversal(bi_tree)








