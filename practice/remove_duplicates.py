from interview_linkedlist import LinkedList

def remove_duplicates(ll):
    current = ll.head
    unique = set()
    unique.add(current.value)
    while current.next:
        if current.next.value in unique:
            current.next = current.next.next
        else:
            unique.add(current.next.value)
            current = current.next

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
print(ll)