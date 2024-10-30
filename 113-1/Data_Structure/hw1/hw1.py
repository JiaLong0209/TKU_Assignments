class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def  __init__(self, head = None):
        self.head = head
        self.size = 0

    def data_to_node(self, data):
        return data if isinstance(data, Node) else Node(data) 
        
    def append_list(self, data_list = None):
        for data in data_list:
            self.append(data)

    def append(self, data = None):
        if self.head is None:
            self.head = self.data_to_node(data)
            return
        new_node = self.data_to_node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current.next is not None:
            print(f'{current.data} -> ', end='')
            current = current.next
        print(f'{current.data} -> {current.next}\n')

    def display_range(self, start, end):
        current = self.head
        index = 1
        while current.next is not None:
            if start <= index < end:
                print(f'{current.data} -> ', end='')
            current = current.next
            index += 1
            if(index == end):
                print(f"{current.data}")
                break

    def get_avg(self):
        sum = 0
        total = 0
        current = self.head
        while current:
            sum += current.data
            total += 1
            current = current.next
        return sum / total
            


data = [25, 27, 24, 22, 26]
ll = LinkedList()

print("\n1.建立每個資料節點，並將所有資料節點串聯起來: ")
ll.append_list(data)
ll.display()

print("\n2.建立好單向鏈結串列後，從各節點中取出資料並且計算平均溫度: ")
print(f'avg_temp: {ll.get_avg()}')

print("\n3.走訪整個串列: ")
ll.display()

print("\n4.顯示從第2節點走訪到第4個節點: ")
ll.display_range(2,4)










