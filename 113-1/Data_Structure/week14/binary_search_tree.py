
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @staticmethod
    def create_node(data):
        return data if isinstance(data, Node) else Node(data)

class bs_tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node.create_node(data)
        else:
            self.add_to(data, self.root)
        

    def add_to(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = Node.create_node(data)
            else: 
                self.add_to(data, current.left)
        elif data > current.data:
            if current.right is None:
                current.right = Node.create_node(data)
            else:
                self.add_to(data, current.right)
        else:
            print("BSTree can not contains the same data!")

    def show(self, method="inorder"):
        if self.root:
            print(f"{method}: ")
            eval(f"self.{method}(self.root)")
            print('\n')

    def preorder(self, current):
        if current: 
            print(current.data, end=" ")
            self.preorder(current.left)
            self.preorder(current.right)

    def inorder(self, current):
        if current: 
            self.inorder(current.left)
            print(current.data, end=" ")
            self.inorder(current.right)

    def postorder(self, current):
        if current: 
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=" ")


data = [60, 25, 93, 18, 34, 78]
tree = bs_tree()


for i in data:
    tree.insert(i)

tree.show("inorder")
tree.show("preorder")
tree.show("postorder")

#       60
#   25      93
# 18  34  78



