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

    def __str__(self):
        result = "Doubly Circular Linked List: "
        current = self.head
        while current is not None:
            result += str(current.value)
            if current.next == self.head:
                result += " <-head-> "
                break
            current = current.next
            result += " <-> "
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

ll = CirularDoublyLinkedList()
ll.append(10)
ll.append(20)
ll.append(40)
print(ll)