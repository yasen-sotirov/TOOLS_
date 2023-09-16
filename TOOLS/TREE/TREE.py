"TREES"   # ДЪРВЕТА


class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children


"ПРИМЕРНО ДЪРВО"
tree_1 = TreeNode(1, [
    TreeNode(2, [TreeNode("5 leaf")]),
    TreeNode(3, [
        TreeNode("6 leaf"),
        TreeNode("7 leaf"),
        TreeNode(8, [TreeNode("11 leaf")])
    ]),
    TreeNode(4, [TreeNode("9 leaf"), TreeNode("10 leaf")])
])


def dfs(root):
    print(root.value)
    for child in root.children:
        dfs(child)

# a = 5
# dfs(tree_1)

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
"""




