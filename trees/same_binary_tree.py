from typing import Optional

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

"""
Run in the neetcode text editor.
"""
class Solution:
  
  # Iterative DFS solution | Time: O(n), Space: O(n)
  # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  #   stack = [(p, q)]

  #   while stack:
  #     node1, node2 = stack.pop()

  #     if not node1 and not node2:
  #       continue
  #     if not node1 or not node2 or node1.val != node2.val:
  #       return False
      
  #     stack.append((node1.right, node2.right))
  #     stack.append((node1.left, node2.left))

  #   return True


  # Recursive DFS solution (best) | Time: O(n), Space: O(n)
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
      return True
    if not p or not q or p.val != q.val:
      return False

    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
