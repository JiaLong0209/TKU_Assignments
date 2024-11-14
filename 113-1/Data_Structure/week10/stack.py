class Stack:
    def __init__(self, capacity = 0):
        self.items = []
        self.capacity = capacity

    def create(self, capacity):
        self.capacity = capacity

    def push(self, data):
        assert not self.full()
        self.items.append(data)

    def pop(self):
        assert not self.is_empty()
        self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def full(self):
        return False if self.capacity is None else self.size() >= self.capacity

    def size(self):
        return len(self.items)

    def peek(self):
        print(not self.is_empty())

        if self.is_empty():
            print(f"The items can not be empty!")
            return None
        return self.items[-1]

    def display(self):
        print(f"====\tDisplay  \t====")
        for i in range(self.size()-1, -1, -1):
            print(f"- Level: {i}\t Data: {self.items[i]}  -")

        print(f"====\tDisplay End\t====\n")

stack = Stack(capacity=3)

# stack.create(3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

for i in range(stack.size()):
    stack.pop()
    stack.display()

print(stack.peek())


