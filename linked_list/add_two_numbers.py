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
  
  # My solution
  # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  #  # Reverse lists
  #   prev = None
  #   cur = l1
  #   while cur:
  #     temp = cur.next
  #     cur.next = prev
  #     prev = cur
  #     cur = temp

  #   prev1 = None
  #   cur1 = l2
  #   while cur1:
  #     temp1 = cur1.next
  #     cur1.next = prev1
  #     prev1 = cur1
  #     cur1 = temp1

  #   cur = prev
  #   first = ""
  #   second = ""
  #   # Save numbers as strings
  #   while cur:
  #     first += str(cur.val)
  #     cur = cur.next

  #   cur1 = prev1
  #   while cur1:
  #     second += str(cur1.val)
  #     cur1 = cur1.next
  #   suma = str(int(first) + int(second))
    
  #   # Build the sum list
  #   node = ListNode(int(suma[-1]), None)
  #   dummy = ListNode(0, node)
  #   for c in range(len(suma) -2, -1, -1):
  #     node.next = ListNode(int(suma[c]), None)
  #     node = node.next
  #   return dummy.next


  # Recursion solution | Time: O(m + n), Space: O(m + n),
  # where m is the length of l1 and n is the length of l2.
  # def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
  #   if not l1 and not l2 and carry == 0:
  #     return None

  #   v1 = l1.val if l1 else 0
  #   v2 = l2.val if l2 else 0

  #   carry, val = divmod(v1 + v2 + carry, 10)

  #   next_node = self.add(
  #     l1.next if l1 else None,
  #     l2.next if l2 else None,
  #     carry
  #   )
  #   return ListNode(val, next_node)

  #   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  #     return self.add(l1, l2, 0)


  # Iteration solution (best) | Time: O(m + n), Space: O(1),
  # where m is the length of l1 and n is the length of l2.
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0

      # new digit
      val = v1 + v2 + carry
      carry = val // 10
      val = val % 10
      cur.next = ListNode(val)

      # update ptrs
      cur = cur.next
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None

    return dummy.next