class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # Insert node into Binary Search Tree
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.data:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        return root

    # Inorder Traversal
    def inorder(self):
        print("Inorder Traversal:")
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.data, end=" ")
            self._inorder(root.right)

    # Preorder Traversal
    def preorder(self):
        print("Preorder Traversal:")
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    # Postorder Traversal
    def postorder(self):
        print("Postorder Traversal:")
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root is not None:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.data, end=" ")


# Create Tree Object
tree = Tree()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.insert(value)

# Traversals
tree.inorder()
tree.preorder()
tree.postorder()