from interview_linkedlist import LinkedList

def sumList(llA, llB):
    l1 = llA.head
    l2 = llB.head

    new = LinkedList()
    
    carry = 0

    while l1 or l2:
        result = carry
        if l1:
            result += l1.value
            l1 = l1.next
        if l2:
            result += l2.value
            l2 = l2.next
        new.append(int(result%10))
        carry = result/10
    return new

ll1 = LinkedList()
ll2 = LinkedList()
ll1.append(7)
ll1.append(1)
ll1.append(8)
print(ll1)
ll2.append(5)
ll2.append(9)
ll2.append(2)
print(ll2)

print(sumList(ll1, ll2))