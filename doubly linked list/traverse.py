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
    
ll = DSLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print(ll)
ll.prepend(5)
print(ll)
ll.traverse()