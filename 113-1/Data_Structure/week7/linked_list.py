class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def  __init__(self, head = None):
        self.head = head
        self.size = 0

    def return_node(self, data):
        return data if isinstance(data, Node) else Node(data) 
        
    def append_data(self, data = None):
        if self.head is None:
            self.head = self.return_node(data)
        else:
            new_node = self.return_node(data)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_head(self, data = None):
        node = self.return_node(data)
        node.next = self.head
        self.head = node
        print(f"Insert data: {data} at head")

    def insert_after(self, prev_node_data,  data = None):
        new_node = self.return_node(data)
        current = self.head
        while current is not None and prev_node_data != current.data:
            current = current.next

        if current is None:
            print(f"Cannot find data: {prev_node_data}")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"Insert data: {data} after data: {current.data}")


    def delete_data(self, target_data = None):
        current = self.head 
        if current and current.data == target_data :
            self.head = current.next
            current = None
            print(f"Delete data: {target_data} at head")
            return
        while current.next:
            if current.next.data == target_data:
                target_node = current.next
                target_node = None
                current.next = current.next.next
                print(f"Delete data: {target_data}")
                return 
            current = current.next
        print(f"Cannot find the {target_data}!")


    def print(self):
        current = self.head
        while current.next is not None:
            print(f'{current.data} -> ', end='')
            current = current.next
        print(f'{current.data} -> {current.next}\n')

ll = LinkedList(Node(10))
ll.append_data(Node(20))
ll.append_data(Node(30))
ll.append_data(40)

for i in range(50, 100+1, 10):
    ll.append_data(i)
ll.print()

ll.delete_data(50)
ll.print()

ll.delete_data(10)
ll.print()

ll.insert_at_head(0)
ll.print()

ll.insert_after(40, 50)
ll.print()


