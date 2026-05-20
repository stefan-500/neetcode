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

  # Recursion solution | Time: O(h), Space: O(h)
  # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
  #   if not root or not p or not q:
  #     return None
    
  #   if(max(p.val, q.val) < root.val):
  #     return self.lowestCommonAncestor(root.left, p, q)
  #   elif (min(p.val, q.val) > root.val):
  #     return self.lowestCommonAncestor(root.right, p, q)
  #   else:
  #     return root


  # Iteration solution (best) | Time: O(h), Space: O(1),
  # where h is the heiht of the tree.
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    cur = root
    while cur:
      if p.val > cur.val and q.val > cur.val:
        cur = cur.right
      elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
      else:
        return cur