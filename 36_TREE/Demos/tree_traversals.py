from queue import Queue
from tree_node import TreeNode


tree = TreeNode(1, [
    TreeNode(2, [
        TreeNode(5)
    ]),
    TreeNode(3, [
        TreeNode(6),
        TreeNode(7),
        TreeNode(8, [
            TreeNode(11)
        ])
    ]),
    TreeNode(4, [
        TreeNode(9),
        TreeNode(10)
    ])
])

def dfs(root):
    print(root.value)
    for child in root.children:
        dfs(child) 

def bfs(root):
    q = Queue()
    q.put(root)
    
    while not q.empty():
        next = q.get()
        print(next.value)
        for child in next.children:
            q.put(child)


dfs(tree)
bfs(tree)