from collections import deque

cq = deque(maxlen=3)
print(cq)
cq.append(10)
cq.append(20)
cq.append(30)
cq.append(40)
print(cq)
print(cq.popleft())
print(cq)
print(cq.clear())
print(cq)

