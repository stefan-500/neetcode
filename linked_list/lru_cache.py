from collections import OrderedDict

"""
Run in the neetcode text editor.
"""

# Brute Force solution | Time: O(n) for each put() and get() operation, Space: O(n)
# class LRUCache:

#   def __init__(self, capacity: int):
#     self.cache = []
#     self.capacity = capacity        

#   def get(self, key: int) -> int:
#     for i in range(len(self.cache)):
#       if self.cache[i][0] == key:
#         tmp = self.cache.pop(i)
#         self.cache.append(tmp)
#         return tmp[1]
#     return -1

#   def put(self, key: int, value: int) -> None:
#     for i in range(len(self.cache)):
#       if self.cache[i][0] == key:
#         tmp = self.cache.pop(i)
#         tmp[1] = value
#         self.cache.append(tmp)
#         return
    
#     if self.capacity == len(self.cache):
#       self.cache.pop(0)

#     self.cache.append([key, value])


# Built-In Data Structure solution | Time: O(1) for each put() and get() operation, Space: O(n) 
# class LRUCache:

#   def __init__(self, capacity: int):
#     self.cache = OrderedDict()
#     self.cap = capacity

#   def get(self, key: int) -> int:
#     if key not in self.cache:
#       return -1
#     self.cache.move_to_end(key)
#     return self.cache[key]

#   def put(self, key: int, value: int) -> None:
#     if key in self.cache:
#       self.cache.move_to_end(key)
#     self.cache[key] = value

#     if len(self.cache) > self.cap:
#       self.cache.popitem(last=False)


# Doubly Linked List solution (best) | Time: O(1) for each put() and get() operation, Space: O(n)
class Node:

  def __init__(self, key, val):
    self.val = val
    self.key = key
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.cap = capacity
    self.cache = {}  # map key to node
    
    # left = LRU, right = MRU
    self.left = Node(0, 0)
    self.right = Node(0, 0)
    self.left.next = self.right
    self.right.prev = self.left

  # Remove node from list
  def remove(self, node: Node):
    prev = node.prev
    nxt = node.next
    prev.next = nxt
    nxt.prev = prev

  # Insert node at right
  def insert(self, node: Node):
    prev = self.right.prev
    nxt = self.right
    
    prev.next = node
    nxt.prev = node
    
    node.next = nxt
    node.prev = prev

  def get(self, key: int) -> int:
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.remove(self.cache[key])            
    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    if len(self.cache) > self.cap:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]