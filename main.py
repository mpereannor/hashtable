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
  



