import queue as q

cq = q.Queue(maxsize=3)
print(cq.empty())
cq.put(10)
cq.put(20)
cq.put(30)
cq.put(40)
print(cq.full())
