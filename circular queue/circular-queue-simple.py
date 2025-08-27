class CircularQueue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.front = -1
        self.rear = -1
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        if (self.rear + 1) % self.maxSize == self.front:
            return True
        return False