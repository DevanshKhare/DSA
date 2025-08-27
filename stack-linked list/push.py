class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.push(50)
print(new_stack.top.value)
