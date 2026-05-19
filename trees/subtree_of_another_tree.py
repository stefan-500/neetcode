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
  
  # Recursive DFS solution (best) | Time: O(m * n), Space: O(m + n),
  # where m is the number of nodes in subRoot and n is the number of nodes in root.
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
      return True
    if not root:
      return False

    if self.sameTree(root, subRoot):
      return True
    return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

  def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not root and not subRoot:
      return True
    if root and subRoot and root.val == subRoot.val:
      return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
    return False