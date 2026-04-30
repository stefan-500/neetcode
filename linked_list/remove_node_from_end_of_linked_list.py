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

  # # My solution  
  # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  #   cur = head
  #   prev = None
  #   # Reverse list
  #   while cur:
  #     tmp = cur.next
  #     cur.next = prev
  #     prev = cur
  #     cur = tmp

  #   slow = prev
  #   if slow.next == None:   # one node in list
  #     return None
  #   fast = prev.next
  #   i = 1
  #   # Remove n-th node
  #   while fast:
  #     if (n - i) == 1:
  #         slow.next = fast.next
  #         break
  #     elif i == n:
  #         slow.next = None
  #         prev = fast
  #         break
  #     else:
  #         i += 1
  #         slow = slow.next
  #         fast = fast.next

  #   # Reverse list back to original
  #   newHead = prev
  #   prev1 = None
  #   while newHead:
  #     tmp = newHead.next
  #     newHead.next = prev1
  #     prev1 = newHead
  #     newHead = tmp
  #   return prev1


  # Brute Force solution | Time: O(n), Space: O(n)
  # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  #   nodes = []
  #   cur = head
  #   while cur:
  #     nodes.append(cur)
  #     cur = cur.next
    
  #   removeIndex = len(nodes) - n
  #   if removeIndex == 0:
  #     return head.next

  #   nodes[removeIndex - 1].next = nodes[removeIndex].next
  #   return head 


  # Iteration (Two Pass) solution | Time: O(n), Space: O(1)
  # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  #   N = 0
  #   cur = head
  #   while cur:
  #     N += 1
  #     cur = cur.next

  #   removeIndex = N - n
  #   if removeIndex == 0:
  #     return head.next

  #   cur = head
  #   for i in range(N - 1):
  #     if (i + 1) == removeIndex:
  #       cur.next = cur.next.next
  #       break
  #     cur = cur.next
  #   return head


  # Two Pointers solution (best) | Time: O(n), Space: O(1)
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0:
      right = right.next
      n -= 1
    
    while right:
      left = left.next
      right = right.next

    left.next = left.next.next    
    return dummy.next