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
