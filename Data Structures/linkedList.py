# storing data in linear order, each object has data and a pointer to the next object
# use cases: used to implement stacks, queus, hash tables and dynamic memory allocation

# first node is head, last node is tail
# doubly linked list has two pointers where the node points to previous and next nodes

# operations

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total = 0 
        while curr.next!=None:
            total+=1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!" )
            return None
        curr_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_index == index: return curr_node.data
            curr_index+=1

    def erase(self, index):
        if index>= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        curr_index = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_index==index:
                last_node.next = curr_node.next
                return
            curr_index+=1

my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)
my_list.display()
        