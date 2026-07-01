from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  # My solution (explanation and AI help)
  # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
  #   res = []
  #   candidates.sort()

  #   def dfs(i, cur, total):
  #     if total == target:
  #       res.append(cur.copy())
  #       return
  #     if i >= len(candidates) or total > target:
  #       return

  #     cur.append(candidates[i])
  #     dfs(i + 1, cur, total + candidates[i])
  #     cur.pop()
      
  #     while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
  #       i += 1
  #     dfs(i + 1, cur, total)
    
  #   dfs(0, [], 0)
  #   return res


  # Backtracking solution (best) | Time: O(n * 2^n), Space: O(n)
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    candidates.sort()

    def dfs(i, cur, total):
      if total == target:
        res.append(cur.copy())
        return
      if total > target or i == len(candidates):
        return

      cur.append(candidates[i])
      dfs(i + 1, cur, total + candidates[i])
      cur.pop()

      while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
        i += 1
      dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res