from queue import Queue


class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


binary_tree = BinaryTreeNode(7,
                    left=BinaryTreeNode(4,
                        left=BinaryTreeNode(2),
                        right=BinaryTreeNode(5,
                            right=BinaryTreeNode(6))),
                    right=BinaryTreeNode(11,
                        left=BinaryTreeNode(8),
                        right=BinaryTreeNode(14,
                            right=BinaryTreeNode(18))))


def dfs_preorder(root):
    if root is None:
        return

    print(root.value)
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None:
        return

    dfs_inorder(root.left)
    print(root.value)
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.value)



def bfs(root):
    q = Queue()
    q.put(root)
    
    while not q.empty():
        next = q.get()
        print(next.value)
        if next.left is not None:
            q.put(next.left)
        if next.right is not None:
            q.put(next.right)


dfs_inorder(binary_tree)
