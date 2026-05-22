from typing import Optional, List
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
  
  # My solution (used BFS solution from maximum_depth_of_binary_tree.py)
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    res = []
    q = deque([root])
    
    while q:
      level = []
      for i in range(len(q)):
        node = q.popleft()
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
        level.append(node.val)
      res.append(level)
    
    return res


  # DFS solution | Time: O(n), Space: O(n)
  # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  #   res = []

  #   def dfs(node, depth):
  #     if not node:
  #       return None
  #     if len(res) == depth:
  #       res.append([])
      
  #     res[depth].append(node.val)
  #     dfs(node.left, depth + 1)
  #     dfs(node.right, depth + 1)

  #   dfs(root, 0)
  #   return res


  # BFS solution (best) | Time: O(n), Space: O(n)
  # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  #   res = []

  #   q = deque()
  #   q.append(root)

  #   while q:
  #     qLen = len(q)
  #     level = []
  #     for i in range(qLen):
  #       node = q.popleft()
  #       if node:
  #         level.append(node.val)
  #         q.append(node.left)
  #         q.append(node.right)
  #     if level:
  #         res.append(level)
  #   return res