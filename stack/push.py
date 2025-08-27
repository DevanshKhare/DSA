class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack.items)