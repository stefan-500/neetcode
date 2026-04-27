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

  # Recursion solution (best) | Time: O(n + m), Space: O(n + m),
  # where n is the length of list1 and m is the length of list2.
  # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  #   if list1 is None:
  #     return list2
  #   if list2 is None:
  #     return list1
  #   if list1.val <= list2.val:
  #     list1.next = self.mergeTwoLists(list1.next, list2)
  #     return list1
  #   else:
  #     list2.next = self.mergeTwoLists(list1, list2.next)
  #     return list2
  
  
  # Iteration solution (best) | Time: O(n + m), Space: O(1),
  # where n is the length of list1 and m is the length of list2.
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy  = ListNode()   # so the linked list is not empty
    tail = dummy

    while list1 and list2:           
      if list1.val < list2.val:
        tail.next = list1
        list1 = list1.next
      else:
        tail.next = list2
        list2 = list2.next
      tail = tail.next
    
    # Connect remaining nodes from the list that still has nodes
    tail.next = list1 or list2
    
    return dummy.next   # ignore the initial node  