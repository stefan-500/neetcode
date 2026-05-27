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
 
 # My solution
  # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
  #   if not root:
  #     return []
    
  #   q = deque()
  #   q.append(root)
  #   res = []

  #   while q:
  #     level = len(q)
  #     for i in range(level):
  #       node = q.popleft()
  #       if node.left:
  #         q.append(node.left)
  #       if node.right:
  #         q.append(node.right)
  #       if i == level - 1:
  #         res.append(node.val)
  #   return res
  

  # DFS solution: Time: O(n), Space: O(n)
  # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
  #   res = []

  #   def dfs(node, depth):
  #     if not node:
  #       return None
  #     if depth == len(res):
  #       res.append(node.val)
      
  #     dfs(node.right, depth + 1)
  #     dfs(node.left, depth + 1)

  #   dfs(root, 0)
  #   return res


  # BFS solution (best): Time: O(n), Space: O(n)
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    q = deque([root])

    while q:
      rightSide = None
      qLen = len(q)

      for i in range(qLen):
        node = q.popleft()
        if node:
          rightSide = node
          q.append(node.left)
          q.append(node.right)
      if rightSide:
        res.append(rightSide.val)
    return res
