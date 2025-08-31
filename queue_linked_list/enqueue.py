class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

lq = Queue()
print(lq)
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.enqueue(40)
lq.enqueue(50)
print(lq)