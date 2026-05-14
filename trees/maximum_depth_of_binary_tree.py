from typing import Optional
from collections import deque

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

  # Breadth First Search solution | Time: O(n), Space: O(n)
  # def maxDepth(self, root: Optional[TreeNode]) -> int:
    # q = deque([root])
    # if root:
    #   q.append(root)      

    # level = 0
    # while q:
    #   for i in range(len(q)):
    #     node = q.popleft()
    #     if node.left:
    #       q.append(node.left)
    #     if node.right:
    #       q.append(node.right)
    #   level += 1
    # return level


  # Iterative DFS solution | Time: O(n), Space: O(n)
  # def maxDepth(self, root: Optional[TreeNode]) -> int:
  #   stack = [[root, 1]]
  #   res = 0

  #   while stack:
  #     node, depth = stack.pop()
      
  #     if node:
  #       res = max(res, depth)
  #       stack.append([node.left, depth + 1])
  #       stack.append([node.right, depth + 1])
  #   return res


  # Recursive DFS solution (best) | Time: O(n), Space: O(h),
  # where n is the number of nodes in the tree and h is the height of the tree.
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))