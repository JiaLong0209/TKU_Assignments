
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data 
        self.next = next
        self.prev = prev

    @staticmethod
    def create_node(data):
        return data if isinstance(data, Node) else Node(data)

class Queue:
    def __init__(self, capacity = None):
        self.capacity = None
        self.size = 0
        self.front = None
        self.rear = None

    def create(self, capacity):
        self.capacity = capacity

    def dequeue(self):
        assert not self.is_empty()
        dequeue_data = self.front.data
        if(self.size == 1):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.prev
        self.size -= 1
        return dequeue_data

    def enqueue(self, data):
        assert not self.full()
        new_node = Node.create_node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.rear
            self.rear.prev = new_node
            self.rear = new_node
        self.size += 1
        return data

    def is_empty(self):
        return self.size == 0

    def full(self):
        return false if self.capacity is None else self.size == self.capacity

    def display(self):
        curr = self.front
        print("(Front to Rear): ", end='')
        while curr:
            print(f"{curr.data} ", end = f"<-> ")
            curr = curr.prev
        print("None")

    def get_front(self):
        assert not self.is_empty()
        return self.front.data

    def get_rear(self):
        assert not self.is_empty()
        return self.rear.data

    def enqueue_list(self, data):
        assert not self.full()
        for i in data:
            self.enqueue(i)

    def get_queue(self):
        queue_list = []
        curr = self.front
        while curr:
            queue_list.append(curr.data)
            curr = curr.prev

        return queue_list


n = 5
queue = Queue()
queue.create(5)

data_list = [i for i in range(10, (n+1) * 10, 10)]


queue.enqueue_list(data_list)

print(queue.get_queue())

queue.display()

# for i in range(10, (n+1) * 10, 10):
#     print(queue.enqueue(i))
#     queue.display()


for i in range(10, (n+1) * 10, 10):
    print(queue.dequeue())
    queue.display()

