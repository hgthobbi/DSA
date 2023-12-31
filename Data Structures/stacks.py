# LIFO
# insert = push
# delete = pop

class Stack:
    def __init__(self):
        self.data = []

    def push(self, node): # time complexity: O(1)
        self.data.append(node)

    def pop(self): # time complexity: O(1)
        self.data.pop()

#use cases: backtracking: finding the correct path through a maze
#compile time memory management: programs use them to store local data and procedure info, nested and recursive functions
# DFS
# undo (pop)/redo (push)

# tips for determining when to use: 
# when you have a previously seen value and you know you need the last seen value first first, you can use a stack
# largest rectangle in a histograph
