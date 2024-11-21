
class Queue:
    def __init__(self, capacity = None):
        self.capacity = None
        self.items = []

    def create(self, capacity):
        self.capacity = capacity

    def dequeue(self):
        assert not self.is_empty()
        return self.items.pop(0)

    def enqueue(self, data):
        assert not self.full()
        self.items.append(data)
        return data

    def is_empty(self):
        return len(self.items) == 0

    def full(self):
        return false if self.capacity is None else len(self.items) >= self.capacity

    def display(self):
        print(self.items)

    def front(self):
        assert not self.is_empty()
        return self.items[0]

n = 5
queue = Queue()
queue.create(5)

for i in range(10, (n+1) * 10, 10):
    queue.enqueue(i)
    queue.display()


for i in range(n):
    queue.dequeue()
    queue.display()

