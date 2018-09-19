import Queue

q = Queue.LifoQueue()

# add items to the head of the queue
for x in range(4):
    q.put("item - " + str(x))

# remove items
while not q.empty():
    print q.get()
