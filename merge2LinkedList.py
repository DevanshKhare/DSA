class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = "Linked List: "
        current= self.head
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index+=1
        return -1
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        temp =  self.get(index)
        if temp.value is not None:
            temp.value = value
    
    def pop(self):
        popped_node = self.head
        self.head = popped_node.next
        self.length -= 1

    def pop_last(self):
        popped_node = self.tail
        temp = self.head
        while temp.next is not popped_node:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.length -= 1

    def remove(self, index):
        prev = self.get(index-1)
        popped_node = prev.next
        prev.next = popped_node.next
        popped_node.next = None
        self.length -= 1

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def middle(self):
        current = self.head
        for _ in range(self.length//2):
            current = current.next
        return current.value

    def middle2(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def remove_duplicate(self):
        unique = set()
        current = self.head
        unique.add(current.value)
        while current.next is not None:
            if current.next.value in unique:
                current.next = current.next.next
                self.length -= 1
            else:
                unique.add(current.next.value)
                current = current.next

    def remove_duplicate2(self, target):
        dummy = Node(0)
        dummy.next = self.head
        current = dummy

        while current.next is not None:
            if current.next.value == target:
                current.next = current.next.next
                self.length -= 1
            else:
                current = current.next
        self.head = dummy.next
    
    def merge(list1, list2):
        list1 = list1.head
        list2 = list2.head
        dummy = Node(0)
        current = dummy

        while list1 and list2:
            if list1.value > list2.value:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
print(ll)

ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(4)
print(ll2)

merged = ll.merge(ll2)
print(merged.value)
print(merged.next.value)
print(merged.next.next.value)
print(merged.next.next.next.value)
print(merged.next.next.next.next.value)
print(merged.next.next.next.next.next.value)



