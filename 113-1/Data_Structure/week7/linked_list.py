class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def  __init__(self, head = None):
        self.head = head

    def return_node(self, data):
        return data if isinstance(data, Node) else Node(data) 
        
    def add_data(self, data = None):
        if self.head is None:
            self.head = self.return_node(data)
        else:
            new_node = self.return_node(data)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node


    def print(self):
        temp = self.head
        while temp.next is not None:
            print(f'{temp.data} -> ', end='')
            temp = temp.next
        print(f'{temp.data} -> {temp.next}')

a = Node(10)
b = Node(20)
c = Node(30)
    

ll = LinkedList()
ll.add_data(b)
ll.add_data(c)
ll.add_data(40)
for i in range(50, 100+1, 10):
    ll.add_data(i)



ll.print()
# print(ll.head.data)
# print(ll.head.data)


