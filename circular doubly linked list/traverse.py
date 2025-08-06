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

ll = CircularDoublyLinkedList()
ll.append(10)
ll.append(20)
ll.append(40)
ll.prepend(5)
ll.prepend(2)
print(ll)
ll.traverse()