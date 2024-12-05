
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def create_node(data):
        return data if isinstance(data, Node) else Node(data)

class BinaryTree():
    def __init__(self):
        self.root = None

    def create(self, data):
        new_node = Node.create_node(data)
        self.root = new_node

    def get_root(self):
        return self.root

    def get_depth(self, node, depth=0):
        if not node: return depth-1
        left_depth = self.get_depth(node.left, depth+1)
        right_depth = self.get_depth(node.right, depth+1)
        print(f"{node.data}, left_depth={left_depth}, right_depth{right_depth}")
        max_depth = max(left_depth, right_depth)
        return max_depth


    def preorder_traversal(self, node, depth=0):
        if not node: return
        print(node.data, end=" ")
        self.preorder_traversal(node.left, depth+1)
        self.preorder_traversal(node.right, depth+1)

    def inorder_traversal(self, node=None, depth=0):
        if not node: return
        self.inorder_traversal(node.left, depth+1)
        print(node.data, end=" ")
        self.inorder_traversal(node.right, depth+1)

    def postorder_traversal(self, node=None, depth=0):
        if not node: return
        self.postorder_traversal(node.left, depth+1)
        self.postorder_traversal(node.right, depth+1)
        print(node.data, end=" ")

    def append(self, data):
        new_node = Node.create_node(data)
        if self.root is None:
            self.root = new_node
        
        cur = self.root 



tree = BinaryTree()
tree.create(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.right.left.left = Node(9)
tree.root.right.left.left.left = Node(10)

#      1   
#   2     3
#  4 5   6 7
# 8     9 
#     10

# print(tree.root.data)

print(f"\npreorder: ")
tree.preorder_traversal(tree.get_root())

print(f"\ninorder: ")
tree.inorder_traversal(tree.get_root())

print(f"\npostorder: ")
tree.postorder_traversal(tree.get_root())

print()
print(f"Depth: {tree.get_depth(tree.get_root())}")










