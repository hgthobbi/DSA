# FIFO
# insert = enqueue
# delete = dequeue

from collections import deque

class Queue:
    def __init__(self): 
        self.data = deque()

    def enqueue(self, node): # time complexity O(1)
        self.data.append(node)
    
    def dequeue(self): # time complexity O(1)
        self.data.popleft()

# use cases
# operating systems
# BFS
# music playlist