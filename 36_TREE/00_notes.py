
"TREES"  # дървета - записки при Едо

from __future__ import annotations


class Category:
    # типизацията може само на едно място
    def __init__(self, name: str, child_category: list[Category]):
        self.name: str = name
        self.child_category = child_category   # рекурсивно


category = Category("Categories", [
    Category("PC and laptops", [
        Category("Desktops", []),
        Category("Laptops", []),
        Category("Peripheral", [
            Category("Mouse", [
                Category("Bluetooth", []),
                Category("With cabal", [])
            ]),
            Category("Keyboard", []),
            Category("Other",[])
        ])
    ]),
    Category("TV's", [
        Category("LCD", []),
        Category("OLED", [])
    ])
])


def visualise(root_category: Category):
    stack = [(root_category, 0)]
    while stack:
        last, indent = stack.pop()
        print(" " * indent, last.name)
        for child in reversed(last.child_category):
            stack.append((child, indent + 2))


print(f"=== Stack iterative:")
visualise(category)

def visual_rec(root_category: Category, indent):
    print(" " * indent, root_category.name)
    for child in root_category.child_category:
        visual_rec(child, indent + 2)


print()
print("=== Call stack rec:")
visual_rec(category, 0)