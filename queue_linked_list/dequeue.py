class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def __str__(self):
        result = "Queue: "
        current = self.front
        while current:
            result += str(current.value)
            if current.next:
                result += " -> "
            current = current.next
        return result

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        removed = self.front
        self.front = self.front.next
        self.length -= 1
        return removed

    def peek(self):
        return self.front

lq = Queue()
print(lq)
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.enqueue(40)
lq.enqueue(50)
print(lq)
lq.dequeue()
print(lq)
print(lq.peek().value)
