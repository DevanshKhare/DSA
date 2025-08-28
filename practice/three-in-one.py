# class ThreeStack:
#     def __init__(self, stack_size):
#         self.stack_size = stack_size
#         self.list = [None] * stack_size * 3
#         self.sizes = [0, 0, 0]

#     def isFull(self, stack_num):
#         return self.sizes[stack_num] == self.stack_size

#     def isEmpty(self, stack_num):
#         return self.sizes[stack_num] == 0
    
#     def indexOfTop(self, stack_num):
#         offset = stack_num * self.stack_size
#         return offset + self.sizes[stack_num] - 1

#     def push(self, stack_num, value):
#         if self.isFull(stack_num):
#             return "Stack is full"
#         self.sizes[stack_num] += 1
#         self.list[self.indexOfTop(stack_num)] = item
    
#     def pop(self, stack_num):
#         if self.isEmpty(stack_num):
#             return "Stack is empty"
#         topval = self.list[self.indexOfTop(stack_num)]
#         self.list[self.indexOfTop(stack_num)] = 0
#         self.sizes[stack_num] -= 1
#         return topval

#     def peek(self, stack_num):
#         if self.isEmpty(stack_num):
#             return "Stack is empty"
#         return self.list[self.indexOfTop(stack_num)]
 






















class ThreeStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * stack_size * 3
        self.sizes = [0] * 3
    
    def isFull(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def isEmpty(self, stack_num):
        return self.sizes[stack_num] == 0

    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1
    
    def push(self, stack_num, value):
        if self.isFull(stack_num):
            return "Stack is full"
        self.sizes[stack_num] += 1
        self.list[self.indexOfTop(stack_num)] = value
    
    def pop(self, value):
        if self.isEmpty(stack_num):
            return "Stack is empty"
        topval = self.list[self.indexOfTop(stack_num)]
        self.list[self.indexOfTop(stack_num)] = None
        self.sizes[stack_num] -= 1
        return topval
    
    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            return "Stack is empty"
        topval = self.list[self.indexOfTop(stack_num)]
        return topval

ts = ThreeStack(3)
print(ts.isEmpty(0))
print(ts.isFull(0))
print(ts.isEmpty(1))
print(ts.isFull(1))
print(ts.isEmpty(2))
print(ts.isFull(2))
ts.push(0, 10)
ts.push(0, 20)
ts.push(0, 30)
ts.push(1, 1)
ts.push(1, 2)
ts.push(1, 3)
ts.push(2, 100)
ts.push(2, 200)
ts.push(2, 300)
print("After insertion")
print(ts.isEmpty(0))
print(ts.isFull(0))
print(ts.isEmpty(1))
print(ts.isFull(1))
print(ts.isEmpty(2))
print(ts.isFull(2))
print(ts.peek(0))
print(ts.peek(1))
print(ts.peek(2))
