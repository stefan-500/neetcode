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

  # Brute Force solution | Time: O(n log n), Space: O(n)
  # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
  #   arr = []

  #   def dfs(node):
  #     if not node:
  #       return
      
  #     arr.append(node.val)
  #     dfs(node.left)
  #     dfs(node.right)

  #   dfs(root)
  #   arr.sort()
  #   return arr[k - 1]
  
  
  # Iterative DFS solution (best) | Time: O(n), Space: O(n)
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root

    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      k -= 1
      if k == 0:
        return curr.val
      curr = curr.right