class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = "Circular Doubly Linked List: "
        current = self.head
        while current:
            result += str(current.value)
            if current.next == self.head:
                result += " <-head-> "
                break
            result += " <-> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print("Node: ", current.value)
            if current.next == self.head:
                break
            current = current.next

    def reverseTraverse(self):
        current = self.tail
        while current:
            print("Reverse Node: ", current.value)
            if current.prev == self.tail:
                break
            current = current.prev

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            if current.next == self.head:
                return -1
            current = current.next
            index+=1
        return -1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def optimalGet(self, index):
        if index < 0 or index >= self.length:
            return None
        current = None
        if index < self.length//2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.prev
        return current

    def set(self, index, value):
        node = self.optimalGet(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length-1:
            self.append(value)
            return
        else:
            new_node = Node(value)
            node = self.optimalGet(index-1)
            new_node.next = node.next
            new_node.prev = node
            node.next = new_node
            node.next.prev = new_node
            return

    def pop_first(self):
        popped_node = self.head
        self.head = self.head.next
        self.tail.next = self.head
        self.head.prev = self.tail
        popped_node.prev = None
        popped_node.next = None
        self.length -= 1

    def pop_last(self):
        popped_node = self.tail
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        popped_node.prev = None
        popped_node.next = None
        self.length -= 1
    
    def remove(self, index):
        if index == 0:
            self.pop_first()
            return
        elif index == self.length - 1:
            self.pop_last()
            return
        popped_node = self.optimalGet(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

ll = CircularDoublyLinkedList()
ll.append(10)
ll.append(20)
ll.append(40)
ll.prepend(5)
ll.prepend(2)
print(ll)
ll.traverse()
ll.reverseTraverse()
print(ll.search(40))
print("Get: ",ll.get(5))
print("Optimal Get:", ll.optimalGet(5))
ll.set(0, 99)
ll.set(2, 35)
ll.set(4, 45)
print(ll)
ll.insert(3, 222)
print(ll)
ll.pop_first()
print(ll)
ll.pop_last()
print("Pop last",ll)
print("tail", ll.tail.value)
print("tail.next", ll.tail.next.value)
print("tail.prev", ll.tail.prev.value)