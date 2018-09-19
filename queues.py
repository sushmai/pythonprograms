#to use priority queue, import heapq

import heapq

#1. heapify() this operation enables you to convert a regulat list to heap.

h = [1,4,2,5,2,6,7,9]
heapq.heapify(h) # gives none if i try to print here 
print(h)

#2. heappush(heap, item) pushes the element into heap 

heapq.heappush(h,7)
print(h)

#3. heapq.heappop(heap) to return the smallest number in the heap
heapq.heappop(h)
print(h)

#heappushpop(heap, item) deletes the smallest item place the item in place
heapq.heappushpop(h,12)
print(h)

#heapreplace(heap, item) deletes the first item and places the value at place 
heapq.heapreplace(h,23)
print(h)
