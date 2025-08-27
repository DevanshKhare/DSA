class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        values = [str(x) for x in reversed(self.items)]
        return "\n".join(values)

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack)

print("popping...",my_stack.pop())

print(my_stack)