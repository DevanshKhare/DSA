class CircularQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        
        result = "Queue Elements: "
        i = self.front
        while True:
            result += str(self.items[i]) + " "
            if i == self.rear:
                break
            i = (i+1)%self.maxSize
        return result

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        if (self.rear + 1) % self.maxSize == self.front:
            return True
        return False
    
    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.maxSize
        self.items[self.rear] = value
        return f"Inserted {value}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        removed_element = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1)%self.maxSize
        return removed_element

cq = CircularQueue(5)
print(cq.is_empty())
print(cq.is_full())
print(cq)

print(cq.enqueue(10))
print(cq.enqueue(20))
print(cq.enqueue(30))
print(cq.enqueue(40))
print(cq.enqueue(50))
print(cq)

print(cq.is_empty())
print(cq.is_full())
print(cq.dequeue())
print(cq.dequeue())
print(cq.is_full())

print(cq)