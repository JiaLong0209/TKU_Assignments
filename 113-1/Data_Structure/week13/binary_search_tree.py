
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
            return

        cur = self.root 
        while cur:
            if new_node.data < cur.data:
                if(cur.left is None):
                    cur.left = new_node
                    return
                cur = cur.left
            else:
                if(cur.right is None):
                    cur.right = new_node
                    return
                cur = cur.right



data = [50, 30, 70, 20 , 40 , 60, 80]
data2 = [10, 5, 15, 3 ,7, 12, 18, 1, 4]
data3 = [40, 20, 60, 10, 30, 50 , 70]

tree = BinaryTree()
for i in data:
    tree.append(i)

print()

tree.inorder_traversal(tree.get_root())


# data
#      50
#   30     70
# 20  40 60  80









