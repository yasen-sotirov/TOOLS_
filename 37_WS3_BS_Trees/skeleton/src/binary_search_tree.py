from src.bst_node import BSTNode


class BinarySearchTree:
    def __init__(self):
        self._root: BSTNode = None

    @property
    def root(self):
        return self._root

    @property
    def height(self):
        raise NotImplementedError()

    def dfs_inorder(self):
        raise NotImplementedError()

    def dfs_preorder(self):
        raise NotImplementedError()

    def dfs_postorder(self):
        raise NotImplementedError()

    def bfs(self):
        raise NotImplementedError()

    def search(self, value):
        raise NotImplementedError()

    def insert(self, value):
        raise NotImplementedError()

    def remove(self, value):
        raise NotImplementedError()
