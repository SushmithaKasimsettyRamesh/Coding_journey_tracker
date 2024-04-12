class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.val, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.val, end=" ")

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal:", end=" ")
inorder_traversal(root)
print("\nPreorder traversal:", end=" ")
preorder_traversal(root)
print("\nPostorder traversal:", end=" ")
postorder_traversal(root)
