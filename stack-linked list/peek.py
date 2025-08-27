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
    
    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def peek(self):
        return self.top

new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
new_stack.push(50)
print(new_stack.top.value)
print(new_stack.pop().value)
print(new_stack.peek().value)