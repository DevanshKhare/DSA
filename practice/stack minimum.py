class Stack:
    def __init__(self):
        self.items = []
        self.minimum = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, value):
        if self.isEmpty():
            self.minimum.append(value)
        if value < self.minimum[-1]:
            self.minimum.append(value)
        self.items.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_value = self.items.pop()
        if popped_value == self.minimum[-1]:
            self.minimum.pop()
        return popped_value

sm = Stack()
sm.push(1)
print(sm.minimum[-1])
sm.push(20)
print(sm.minimum[-1])
sm.push(40)
print(sm.minimum[-1])
sm.push(3)
print(sm.minimum[-1])
