from typing import Optional
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

"""
Run in the neetcode text editor.
"""
class Solution:

  # My solution
  # def hasCycle(self, head: Optional[ListNode]) -> bool:
  #   seen = defaultdict(int)
  #   i = 0

  #   while head:
  #     nxt = head.next
  #     if nxt in seen.values():
  #       return True
  #     seen[i] = nxt
  #     head = head.next
  #     i += 1
  #   return False


  # Hash Set solution | Time: O(n), Space: O(n)
  # def hasCycle(self, head: Optional[ListNode]) -> bool:
  #   seen = set()
  #   cur = head
    
  #   while cur:
  #     if cur in seen:
  #       return True
  #     seen.add(cur)
  #     cur = cur.next
  #   return False


  # Fast and Slow Pointers solution (best) | Time: O(n), Space: O(1)
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head

    while fast and fast.next:   # and fast.next because fast moves two steps
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False