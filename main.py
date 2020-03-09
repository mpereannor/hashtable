capacity = 50
class Node: 
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None
  def __str__(self):
    return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
  def __repr__(self):
    return str(self)

#hash table with separate chaining
class HashTable: 
  def __init__(self):
    self.capacity = capacity
    self.size = 0
    self.buckets = [None] * self.capacity

#generate a hash for a given key
#input: key - string
#output: index from 0 to self.capacity

def hash(self, key): 
  hashsum = 0
  
  #for each character in the key 
  for idx, c in enumerate(key):
    #add (index + length of key) **
    #current char code
    hashsum += (idx + len(key)) ** ord(c)
    #perform modulus to keep hashsum in range
    #of (0 and self.capacity - 1)
    hashsum = hashsum % self.capacity
  return hashsum 

def insert(self, key, value):
  #increment size
  self.size += 1
  #compute index of key using hash function
  index = self.hash(key)
  #create new node if bucket at index is empty
  node = self.buckets[index]
  if node is None:
    self.buckets[index] = Node(key, value)
    return
  prev = node
  while node is not None: 
    #collision, at least a node at this index
    #iterate to the end of the list and add new node with provided key / value 
    prev  = node
    node = node.next
    prev.next = Node(key, value)
  
def find(self, key):
  #compute index of key using hash function 
  index = self.hash(key)
  #go to first node in list at bucket
  node = self.buckets[index]
  #traverse linked list at this node 
  while node is not None and node.key != key:
    node =  node.next
  #node is the requested key/value pair or None
  if node is None:
    return None

  else: 
    return node.value

def remove(self, key):
  #compute index of key using hash function
  index = self.hash(key)
  node = self.buckets[index]
  prev = None

  #iterate to the requested node 
  while node is not None and node.key != key: 
    prev = node
    node = node.next
    #node is the requested node open
  if node is None: 
    return None
  else: 
    self.size -= 1
    result = node.value
    if prev is None:
      self.buckets[index] = node.next
    else:
      prev.next = prev.next.next

    return result