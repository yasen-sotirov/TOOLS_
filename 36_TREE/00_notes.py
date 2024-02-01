"TREES"  # дървета - записки при Едо


# from __future__ import annotations
# импортирам^ аки искам type hinting при child: list[Category]


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


"ОБХОЖДАНЕ ИТЕРАТИВНО"
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



"ОБХОЖДАНЕ РЕКУРСИВНО"  # Preorder
# def visual_rec(category: Category, indent=0):
#     print(" " * indent, category.name)
#
#     for child in category.child:
#         visual_rec(child, indent + 2)
#
# visual_rec(categories)