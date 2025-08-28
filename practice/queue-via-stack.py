class Stack:
    """
    Stack:
        A basic stack implementation using a Python list.
        Methods:
            __init__: Initializes an empty stack.
            __len__: Returns the number of elements in the stack.
            push(value): Adds an element to the top of the stack.
            pop(): Removes and returns the top element from the stack. Returns "Empty Stack" if the stack is empty.
    QueueviaStack:
        Implements a queue using two stacks (inStack and outStack).
        Methods:
            __init__: Initializes two stacks for queue operations.
            enqueue(item): Adds an item to the queue (pushes onto inStack).
            dequeue(): Removes and returns the oldest item from the queue.
                - Moves all items from inStack to outStack (reverses order).
                - Pops the top item from outStack (which is the oldest item in the queue).
                - Moves remaining items back to inStack for further operations.
                - Returns the dequeued item.
                # This ensures FIFO behavior using two LIFO stacks.
    Example usage:
        print(cq.dequeue())  # Removes and prints the first inserted element (1)
        print(cq.dequeue())  # Removes and prints the next oldest element (2)
    """
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)

    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        if len(self.list) == 0:
            return "Empty Stack"
        return self.list.pop()

class QueueviaStack():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    
    def enqueue(self, item):
        self.inStack.push(item)
    
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop() #this is the 1st inserted element in the queue so we removed it and then we are placing rest other elements back into the inStack for further push operations
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

cq = QueueviaStack()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())
cq.enqueue(4)
print(cq.dequeue())


