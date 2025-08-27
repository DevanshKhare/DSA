class CircularQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        if (self.rear + 1)%self.maxSize == self.front:
            return True
        return False
    
    def enqueue(self, value):
        if self.is_full():
            return "Queue is Full"
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.maxSize
        self.items[self.rear] = value
        return f"Inserted {value}"

cq = CircularQueue(5)
print(cq.is_empty())
print(cq.is_full())
print(cq.enqueue(10))
print(cq.enqueue(20))
print(cq.enqueue(30))
print(cq.enqueue(40))
print(cq.enqueue(50))
print(cq.is_empty())
print(cq.is_full())