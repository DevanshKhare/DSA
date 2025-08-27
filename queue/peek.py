class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        values = [str(x) for x in self.items]
        return " ".join(values)

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, element):
        self.items.append(element)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]
    
    def delete(self):
        self.items = []

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)