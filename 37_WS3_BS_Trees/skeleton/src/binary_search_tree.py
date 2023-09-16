from src.bst_node import BSTNode
from collections import deque


class BinarySearchTree:
    def __init__(self):
        self._root: BSTNode = None

    @property
    def root(self):
        return self._root

    @property
    def height(self):
        return self.height_rec(self._root)

    def height_rec(self, node):
        if node is None:
            return 0
        left_height = self.height_rec(node.left)
        right_height = self.height_rec(node.right)
        return max(left_height, right_height) + 1




    def dfs_inorder(self):
        result = []
        self.dfs_inorder_rec(self._root, result)
        return result

    def dfs_inorder_rec(self, node, result):
        if node:
            self.dfs_inorder_rec(node.left, result)
            result.append(node.value)
            self.dfs_inorder_rec(node.right, result)




    def dfs_preorder(self):
        result = []
        self.dfs_preorder_rec(self._root, result)
        return result

    def dfs_preorder_rec(self, node, result):
        if node:
            result.append(node.value)
            self.dfs_preorder_rec(node.left, result)
            self.dfs_preorder_rec(node.right, result)




    def dfs_postorder(self):
        result = []
        self.dfs_postorder_rec(self._root, result)
        return result

    def dfs_postorder_rec(self, node, result):
        if node:
            self.dfs_postorder_rec(node.left, result)
            self.dfs_postorder_rec(node.right, result)
            result.append(node.value)




    def bfs(self):
        result = []
        if self._root is not None:
            queue = deque()
            queue.append(self._root)

            while queue:
                node = queue.popleft()
                result.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result




    def search(self, value):
        return self.search_rec(self._root, value)

    def search_rec(self, current_node, value):
        if current_node is None:
            return False

        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self.search_rec(current_node.left, value)
        else:
            return self.search_rec(current_node.right, value)




    def insert(self, value):
        new_node = BSTNode(value)
        if self._root is None:
            self._root = new_node
        else:
            self.insert_rec(self._root, new_node)

    def insert_rec(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_rec(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_rec(current_node.right, new_node)




    def remove(self, value):
        if self.search(value):
            self.remove_rec(self._root, value)

    def remove_rec(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self.remove_rec(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.remove_rec(current_node.right, value)

        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_node = self._find_min_node(current_node.right)
            current_node.value = min_node.value
            current_node.right = self.remove_rec(current_node.right, min_node.value)

        return current_node

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node



# ====================================================


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 9]

    for value in values:
        bst.insert(value)

    root = bst._root
    print(root.value)  # Извежда: 5
    print(root.left.value)  # Извежда: 3
    print(root.left.left.value)  # Извежда: 1
    print(root.left.right.value)  # Извежда: 4
    print(root.right.value)  # Извежда: 7
    print(root.right.left.value)  # Извежда: 6
    print(root.right.right.value)  # Извежда: 9