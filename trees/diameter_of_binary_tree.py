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

  # Brute Force solution | Time: O(n^2), Space: O(n)
  # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
  #   if not root:
  #     return 0

  #   leftHeight = self.maxHeight(root.left)
  #   rightHeight = self.maxHeight(root.right)
  #   diameter = leftHeight + rightHeight
  #   sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
  #   return max(diameter, sub)

  # def maxHeight(self, root: Optional[TreeNode]) -> int:
  #   if not root:
  #     return 0
    
  #   return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


  # Recursive DFS solution (best) | Time: O(n), Space: O(h),
  # where n is the number of nodes in the tree and h is the height of the tree.
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(root):
      nonlocal res

      if not root:
        return 0
      left = dfs(root.left)
      right = dfs(root.right)
      res = max(res, left + right)

      return 1 + max(left, right)

    dfs(root)
    return res