# search time of O(1) on average, worst case is O(n)
# specific way of implementing a dictionary

dictionary = {
    'a': 1,
    'b': 9,
    'c': 'nebraska',
    'd': True
}

# dictionary insert
dictionary['e'] = False

# dictionary delete
del dictionary['a']

# dictionary search
print(dictionary['c'])

# direct access table (array) has a universe of keys. Some are in use and they point to data. insert, delete, search are O(1)

# hashtable space is O(K) where K is the number of actual keys. Hash functions maps keys to location in the table that holds data. 
# Hashing can result in collision, where two values are mapped to one kay. To resolve this we use linked lists

# the hash function needs to maximize randomness and produce the least number of collisions
# examples: division, multiplication, universal hashing, dynamic perfect hashing, static perfect hashing

#hashing by division h(k) = k mod m where m is the size of the table


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
  
    def _hash(self, key):
        return hash(key) % self.capacity
  
    def insert(self, key, value):
        index = self._hash(key)
  
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
  
    def search(self, key):
        index = self._hash(key)
  
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
  
        raise KeyError(key)
  
    def remove(self, key):
        index = self._hash(key)
  
        previous = None
        current = self.table[index]
  
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
  
        raise KeyError(key)
  
    def __len__(self):
        return self.size
  
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
  
  
# Driver code
if __name__ == '__main__':
  
    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)
  
    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)
  
    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False
  
    # Get the value for a key
    print(ht.search("banana"))  # 2
  
    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4
  
    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3