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
                result += "--> head"
                break
            result += "-> "
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

print(csll)