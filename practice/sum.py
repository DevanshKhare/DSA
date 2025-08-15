from interview_linkedlist import LinkedList

def sumList(llA, llB):
    l1 = llA.head
    l2 = llB.head

    new = LinkedList()

    result1 = ""
    result2 = ""

    while l1 or l2:
        if l1:
            result1+= str(l1.value)
            l1 = l1.next
        if l2:
            result2+= str(l2.value)
            l2 = l2.next
    result1 = int(result1[::-1])
    result2 = int(result2[::-1])

    result = result1 + result2
    result = str(result)
    result = int(result)

    while result:
        d = result%10
        new.append(d)
        result = result//10
    return new.head

ll1 = LinkedList()
ll2 = LinkedList()
ll1.append(7)
ll1.append(1)
ll1.append(6)
print(ll1)
ll2.append(5)
ll2.append(9)
ll2.append(2)
print(ll2)

sumList(ll1, ll2)