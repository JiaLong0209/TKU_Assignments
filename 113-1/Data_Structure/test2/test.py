class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

n4 = Node(60, None)
n3 = Node(50, n4)
n2 = Node(40, n3)
n1 = Node(30, n2)
current = n1

while current is not None:
    if current.next and current.next.data == 50:
        current.next = current.next.next
        break
    current = current.next

while current is not None:
    print(3-current.data, end="->")
    current = current.next
print("None")




