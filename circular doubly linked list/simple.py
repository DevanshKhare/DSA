class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CirularDoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

ll = CirularDoublyLinkedList(10)
print(ll.length)