class Node:
    def __init__(value, self):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = "Linked List: "
        current = self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " -> "
            current = current.next
        return result

ll = LinkedList()
print(ll)