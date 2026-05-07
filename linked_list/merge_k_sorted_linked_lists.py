from typing import Optional, List

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
  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #   if not lists:
  #     return

  #   dummy = ListNode(0)
  #   merged = []

  #   # append node values to a list
  #   for l in lists:
  #     cur = l
  #     while cur:
  #       merged.append(cur.val)
  #       cur = cur.next

  #   merged = sorted(merged)
  #   prev = ListNode(merged[0])
  #   dummy.next = prev
  #   for i in range(1, len(merged)):
  #     node = ListNode(merged[i], )
  #     prev.next = node
  #     prev = node
  #   return dummy.next


  # My 2. solution (used code from merge_two_sorted_linked_lists.py, and AI helped)
  # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  #   dummy  = ListNode()   # so the linked list is not empty
  #   tail = dummy

  #   while list1 and list2:          
  #     if list1.val < list2.val:
  #       tail.next = list1
  #       list1 = list1.next
  #     else:
  #       tail.next = list2
  #       list2 = list2.next
  #     tail = tail.next
    
  #   # Connect remaining nodes from the list that still has nodes
  #   tail.next = list1 or list2
  #   return dummy.next   # ignore the initial node  
    
  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #   if not lists:
  #     return

  #   k = len(lists)
  #   if k >= 2:
  #     k -= 2
  #     res = self.mergeTwoLists(lists.pop(0), lists.pop(0))
  #   else:
  #     return lists[0]   # only list (already sorted)

  #   while k:
  #     res = self.mergeTwoLists(res, lists.pop(0))
  #     k -= 1
  #   return res


  # Brute Force solution | Time: O(n log n), Space: O(n)
  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #   nodes = []
  #   for lst in lists:
  #     while lst:
  #       nodes.append(lst.val)
  #       lst = lst.next
  #   nodes.sort()

  #   res = ListNode(0)
  #   cur = res
  #   for node in nodes:
  #     cur.next = ListNode(node)
  #     cur = cur.next
  #   return res.next


  # Divide and Conquer Recursive solution | Time: O(n log k), Space: O(log k),
  # where k is the total number of lists and n is the total number of nodes across k lists.
  # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  #   if not lists or len(lists) == 0:
  #     return None
  #   return self.divide(lists, 0, len(lists) - 1)

  # def divide(self, lists, l, r):
  #   if l > r:
  #     return None
  #   if l == r:
  #     return lists[l]
    
  #   mid = l + (r - l) // 2
  #   left = self.divide(lists, l, mid)
  #   right = self.divide(lists, mid + 1, r)

  #   return self.conquer(left, right)

  # def conquer(self, l1, l2):
  #   dummy = ListNode(0)
  #   curr = dummy

  #   while l1 and l2:
  #     if l1.val <= l2.val:
  #       curr.next = l1
  #       l1 = l1.next
  #     else:
  #       curr.next = l2
  #       l2 = l2.next
  #     curr = curr.next
    
  #   curr.next = l1 or l2
  #   return dummy.next        
  
  
  # Divide and Conquer Iterative solution (best) | Time: O(n log k), Space: O(k),
  # where k is the total number of lists and n is the total number of nodes across k lists.
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists or len(lists) == 0:
      return None
    
    while len(lists) > 1:
      mergedLists = []
      for i in range(0, len(lists), 2):
        l1 = lists[i]
        l2 = lists[i + 1] if (i + 1) < len(lists) else None   # handled by mergeList() if null
        mergedLists.append(self.mergeList(l1, l2))
      lists = mergedLists
    return lists[0]

  def mergeList(self, l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
      if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next

    tail.next = l1 or l2
    return dummy.next