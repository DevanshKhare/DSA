class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CirularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
        self.length += 1

ll = CirularDoublyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.length)