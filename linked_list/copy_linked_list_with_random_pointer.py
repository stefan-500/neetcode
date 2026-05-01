from typing import Optional
from collections import defaultdict

# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


"""
Run in the neetcode text editor.
"""
class Solution:
  
  # Hash Map (One Pass) | Time: O(n), Space: O(n)
  # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
  #   oldToCopy = defaultdict(lambda: Node(0))
  #   oldToCopy[None] = None

  #   cur = head
  #   while cur:
  #     oldToCopy[cur].val = cur.val
  #     oldToCopy[cur].next = oldToCopy[cur.next]
  #     oldToCopy[cur].random = oldToCopy[cur.random]
  #     cur = cur.next
  #   return oldToCopy[head]


  # Hash Map (Two Pass) solution (best) | Time: O(n), Space: O(n)
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = { None : None }  # initial mapping for None case
    cur = head
    while cur:
      copy = Node(cur.val)
      oldToCopy[cur] = copy
      cur = cur.next
    
    cur = head
    while cur:
      copy = oldToCopy[cur]
      copy.next = oldToCopy[cur.next]
      copy.random = oldToCopy[cur.random]
      cur = cur.next
    
    return oldToCopy[head]