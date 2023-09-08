class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child=None
        self.right_child=None
    
class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left_child == None:
                curr_node.left_child = node(value)
            else:
                self._insert(value, curr_node.left_child)
        elif value>curr_node.value:
            if curr_node.right_child == None:
                curr_node.right_child = node(value)
            else:
                self._insert(value,curr_node.right_child)
        else:
            print ("Value already in tree!")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, curr_node):
        if curr_node != None:
            self._printTree(curr_node.left_child)
            print(str(curr_node.value))
            self._printTree(curr_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height
        left_height = self._height(curr_node.left_child, curr_height+1)
        right_height = self._height(curr_node.right_child, curr_height+1)
        return max(left_height, right_height)



def fillTree(tree, num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fillTree(tree)

tree.printTree()
print("tree hieght is: " + str(tree.height()))
