from collections import defaultdict
from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

"""
Run in the neetcode text editor.
"""
class Solution:

  # My solution (ChatGPT helped significantly)
  # def reorderList(self, head: Optional[ListNode]) -> None:
    # prev = defaultdict(ListNode)
    # previous = None
    # cur = head
    # # save prev node for each node
    # while cur:
    #   prev[cur] = previous
    #   previous = cur
    #   cur = cur.next

    # r = previous    # last node
    # l = head
    # while l != r and l.next != r:   # same mid node or adjecent pointers (even)
    #   next_l = l.next
    #   prev_r = prev[r]

    #   l.next = r
    #   r.next = next_l

    #   l = next_l
    #   r = prev_r
    # if l == r:
    #   l.next = None
    # else:
    #   r.next = None

  
  # Recursion solution | Time: O(n), Space: O(n)
  # def reorderList(self, head: Optional[ListNode]) -> None:
  #   def rec(root: ListNode, cur: ListNode) -> ListNode:
  #     if not cur:
  #       return root

  #     root = rec(root, cur.next)
  #     if not root:
  #       return None

  #     tmp = None
  #     if root == cur or root.next == cur:
  #       cur.next = None
  #     else:
  #       tmp = root.next
  #       root.next = cur
  #       cur.next = tmp

  #     return tmp

  #   head = rec(head, head.next)


  # Brute Force solution | Time: O(n), Space: O(n)
  # def reorderList(self, head: Optional[ListNode]) -> None:
  #   if not head:
  #     return

  #   nodes = []
  #   cur = head
  #   while cur:
  #     nodes.append(cur)
  #     cur = cur.next

  #   i = 0
  #   j = len(nodes) - 1
  #   while i < j:
  #     nodes[i].next = nodes[j]
  #     i += 1
  #     if i >= j:
  #       break
  #     nodes[j].next = nodes[i]
  #     j -= 1
  #   nodes[i].next = None


  # Reverse and Merge solution (best) | Time: O(n), Space: O(1)
  def reorderList(self, head: Optional[ListNode]) -> None:
    slow = head
    fast = head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    second = slow.next
    slow.next = None
    prev = None
    while second:
      tmp = second.next
      second.next = prev
      prev = second
      second = tmp

    first = head
    second = prev
    while second:
      tmp1 = first.next
      tmp2 = second.next
      first.next = second
      second.next = tmp1
      first = tmp1
      second = tmp2