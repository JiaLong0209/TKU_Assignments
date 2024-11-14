class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def data_to_node(data):
    return data if isinstance(data, Node) else Node(data)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def create(self, capacity):
        self.capacity = capacity

    def is_empty(self):
        return self.top is None

    def full(self):
        if sefl.capacity is None:
            return False
        return self.size >= self.capacity

    def peek(self):
        assert not self.is_empty()
        return self.top.data

    def push(self, data):
        new_node = data_to_node(data)

        if self.is_empty(): 
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.size += 1
        return new_node.data

    def pop(self):
        assert not self.is_empty()
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def display(self):
        print(f"====\tDisplay  \t====")
        level, curr = self.size, self.top
        
        while curr:
            print(f"- Level: {level}\t Data: {curr.data}  -")
            curr = curr.next
            level -= 1

        print(f"====\tDisplay End\t====\n")

stack = Stack()

stack.create(3)
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

for i in range(stack.size):
    stack.pop()
    stack.display()

# print(stack.peek())


