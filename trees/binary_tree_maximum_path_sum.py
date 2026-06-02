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

  # # DFS solution | Time: O(n^2), Space: O(n)
  # def maxPathSum(self, root: Optional[TreeNode]) -> int:
  #   res = -float('inf')
  #   def dfs(root):
  #     nonlocal res
  #     if not root:
  #       return
  #     left = self.getMax(root.left)
  #     right = self.getMax(root.right)
  #     res = max(res, root.val + left + right)
  #     dfs(root.left)
  #     dfs(root.right)
  #   dfs(root)
  #   return res

  # def getMax(self, root: Optional[TreeNode]) -> int:
  #   if not root:
  #     return 0
    
  #   left = self.getMax(root.left)
  #   right = self.getMax(root.right)
  #   path = root.val + max(left, right)
  #   return max(0, path)
  

  # DFS optimal solution (best) | Time: O(n), Space: O(n)
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [root.val]

    def dfs(root):
      if not root:
        return 0
      
      leftMax = dfs(root.left)
      rightMax = dfs(root.right)
      leftMax = max(leftMax, 0)
      rightMax = max(rightMax, 0)

      res[0] = max(res[0], root.val + leftMax + rightMax)
      return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]