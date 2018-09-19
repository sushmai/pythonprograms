"""
Algorithm
The following steps can be seen as a flow chart to the operation of the Circular Queue:

Initialize the queue, size of the queue (maxSize), head and tail pointers
    Enqueue:
Check if the number of elements (size) is equal to the size of the queue (maxSize):
If yes, throw error message "Queue Full!"
If no, append the new element and increment the tail pointer
    Dequeue:
Check if the number of elements (size) is equal to 0:
If yes, throw error message "Queue Empty!"
If no, increment head pointer
    Size:
If tail>=head, size = tail - head
if head>tail, size = maxSize - (head - tail)

"""

class CircularQueue:
    #constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 8


    # Adding elements to the queue
    def enqueue(self, data):
        if self.size() == self.maxSize-1:
            return("Queue Is Full!!")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    # removing elements from the queue
    def dequeue(self):
        if self.size() == 0:
            return("Queue Empty !")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data
    # calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return(self.tail-self.head)
        return(self.maxSize - (self.head-self.tail))


q = CircularQueue()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())






























        
