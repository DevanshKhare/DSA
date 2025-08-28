class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def __str__(self):
        return str(self.stacks)
    
    def push(self, value):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([]) #create new stack
        self.stacks[-1].append(value)
    
    def pop(self):
        if not self.stacks:
            return "Stack is empty"
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop() #remove empty stack
        return value
    
    def popAt(self, index):
        if not self.stacks[index]:
            return "Pop from empty sub-stack"
        value = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return value

plate = PlateStack(3)
plate.push(1)
plate.push(2)
plate.push(3)
print(plate)
plate.push(4)
plate.push(5)
plate.push(6)
plate.push(7)
plate.push(8)
plate.push(9)
print(plate)
plate.pop()
print(plate)
plate.popAt(0)
print(plate)

