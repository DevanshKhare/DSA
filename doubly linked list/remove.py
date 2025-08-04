class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = "DSLinkedList: "
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += "<->"
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def traverse(self):
        current = self.head
        while current is not None:
            print("Node: ", current.value)
            current = current.next
    
    def reverseTraverse(self):
        current = self.tail
        while current is not None:
            print("Reverse Node: ", current.value)
            current = current.prev

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if value == current.value:
                return index
            index+=1
            current = current.next
        return -1

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        print(current.value)

    def optimalGet(self, index):
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
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def optimalSet(self, index, value):
        node = self.optimalGet(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        node = self.optimalGet(index-1)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
        self.length += 1

    def popFirst(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def popLast(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            print("self.tail.prev.val", self.tail.value)
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if not self.head:
            return
        if index == 0:
            popped_node = self.popFirst()
            return popped_node
        elif index == self.length-1:
            popped_node = self.popLast()
            return popped_node
        else:
            popped_node = self.optimalGet(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.length -= 1
            return popped_node

ll = DSLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print(ll)
ll.prepend(5)
print(ll)
ll.traverse()
ll.reverseTraverse()
print(ll.search(5))
print("before getting item at 4")
ll.get(4)
ll.optimalGet(4)
ll.set(4, 12)
ll.optimalSet(1, 25)
print(ll)
ll.insert(4, 52)
print(ll)
ll.popFirst()
print(ll)
# print("Before popping last")
# print(ll.popLast().value)
print()
print(ll.remove(0).value)