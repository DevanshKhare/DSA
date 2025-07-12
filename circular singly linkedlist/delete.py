class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = "CSLinkedList: "
        current = self.head

        while current is not None:
            result += str(current.value)
            if current.next == self.head:
                result += " --> head"
                break
            result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        else:
            current = self.head
            for  _ in range(index -1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1
    
    def search(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            if current.next == self.head:
                break
            index += 1
            current = current.next
        return -1
    
    def get(self, index):
        current = self.head

        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def pop_first(self):
        if self.head is None:
            return None
        if self.head.next == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.length -= 1

    def pop_last(self):
        if self.head is None:
            return None
        if self.head.next == self.head:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
            popped_node.next = None
        self.length -= 1
    
    def remove(self, index):
        if self.head is None:
            return None
        elif index == 0:
            self.pop_first()
        elif self.head.next == self.head:
            self.head = None
            self.tail = None
            return
        else:
            prev = self.get(index-1)
            popped_node = prev.next
            prev.next = popped_node.next
            popped_node.next = None
        self.length -= 1
    
    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

csll = CSLinkedList()
csll.append(10)
csll.append(20)
csll.append(20)
csll.append(30)
csll.append(40)
csll.append(40)
csll.prepend(0)
csll.prepend(5)
csll.append(45)
csll.insert(0,85)
print(csll)
print(csll.search(45))
print(csll.get(0))
print(csll.set(5, 37))
csll.pop_first()
print(csll)
csll.pop_last()
print(csll)
csll.remove(3)
print(csll)
csll.delete_all()
print(csll)