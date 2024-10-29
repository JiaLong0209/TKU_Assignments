class Node: 
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def print(self):
        print(self.data)

def data_to_node(data):
    return data if isinstance(data, Node) else Node(data)

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0;

    def append(self, data):
        if(self.head == None): 
            self.head = data_to_node(data)
            self.size += 1
            return
        new_node = data_to_node(data)
        curr = self.head 
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.size += 1
        new_node.prev = curr

    def print(self):
        curr = self.head
        while curr:
            print(f'{curr.data}', end=' <-> ')
            curr = curr.next
        print(f'{curr}\n')

    def at(self, index):
        if index == self.size: 
            print(f"{index} is out of index!")
            return None
        curr = self.head
        for i in range(index):
            print(f'-- {curr.data}')
            if curr.next:
                curr = curr.next
            else:
                return curr
        return curr


    def delete(self, data):
        pass



ll = DoublyLinkedList()
n2 = Node(20)



# append
ll.append(10)
ll.append(n2)

for i in range(50, 100+1, 10):
    ll.append(i)
ll.print()


ll.print()

# print(ll.size)

ll.at(4).print()
ll.at(7).print()
















