class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node ##next points back to itself in case of 1 item
        self.head = new_node
        self.tail = new_node
        self.length = 1
