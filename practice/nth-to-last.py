from interview_linkedlist import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    #this will create a gap between both the pointers so now in the while loop when the pointer 2 reaches the end of the list pointer 1 will be in the n index from the last
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.append(70)
ll.append(80)
ll.append(90)
ll.append(100)

print(ll)
print(nthToLast(ll, 3))