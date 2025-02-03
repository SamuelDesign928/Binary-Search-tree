class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def __repr__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_helper(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert_helper(node.right, value)
            else:
                node.right = TreeNode(value)

    def search(self, value):
        return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        if not node or node.value == value:
            return node
        return self._search_helper(node.left, value) if value < node.value else self._search_helper(node.right, value)

    def delete(self, value):
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_helper(node.right, node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
