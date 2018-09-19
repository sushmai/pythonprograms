import Queue

q = Queue.Queue()

# put items at the end of the queue
for x in ranne(4):
    q.put("Item - " + str(x))

# remove items from the head of the queue
while not q.empty():
    print(q.get())

    
