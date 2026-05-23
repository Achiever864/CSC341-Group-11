class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Get height of node
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factor
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    # Right Rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        return x

    # Left Rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    # Insert node
    def insert(self, root, key):

        # Step 1: Normal BST Insert
        if not root:
            return Node(key)

        elif key < root.data:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3: Get balance factor
        balance = self.get_balance(root)

        # LEFT LEFT CASE
        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)

        # RIGHT RIGHT CASE
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        # LEFT RIGHT CASE
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RIGHT LEFT CASE
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


tree = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = tree.insert(root, value)

print("Inorder Traversal:")
tree.inorder(root)

print("\n\nPreorder Traversal:")
tree.preorder(root)

print("\n\nPostorder Traversal:")
tree.postorder(root)