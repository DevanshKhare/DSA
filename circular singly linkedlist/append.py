class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        new_node.next= self.head
        self.length += 1
    
csll = CSLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.append(40)
print(csll)