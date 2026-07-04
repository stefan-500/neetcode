from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  # My solution (used previous problem solutions)
  # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
  #   res = []
  #   subset = []
  #   nums.sort()

  #   def dfs(i):
  #     if i >= len(nums):
  #       res.append(subset.copy())
  #       return
  #     subset.append(nums[i])
  #     dfs(i + 1)
  #     subset.pop()
      
  #     while i + 1 < len(nums) and nums[i] == nums[i+1]:
  #       i += 1
  #     dfs(i + 1)
    
  #   dfs(0)
  #   return res


  # Brute Force solution | Time: O(n * 2^n) | Space: O(2^n).
  # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
  #   res = set()

  #   def backtrack(i, subset):
  #     if i == len(nums):
  #       res.add(tuple(subset))
  #       return
      
  #     subset.append(nums[i])
  #     backtrack(i + 1, subset)
  #     subset.pop()
  #     backtrack(i + 1, subset)

  #   nums.sort()
  #   backtrack(0, [])
  #   return [list(s) for s in res]


  # Backtracking solution (best) | Time: O(n * 2^n) | Space: O(n).
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def backtrack(i, subset):
      if i == len(nums):
        res.append(subset[::])
        return
      
      subset.append(nums[i])
      backtrack(i + 1, subset)
      subset.pop()

      while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
      backtrack(i + 1, subset)

    backtrack(0, [])
    return res