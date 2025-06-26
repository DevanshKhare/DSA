class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = "Linked List: "
        current= self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index+=1
        return -1
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set(self, index, value):
        temp =  self.get(index)
        if temp.value is not None:
            temp.value = value
    
    def pop(self):
        popped_node = self.head
        self.head = popped_node.next
        self.length -= 1

    def pop_last(self):
        popped_node = self.tail
        temp = self.head
        while temp.next is not popped_node:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1