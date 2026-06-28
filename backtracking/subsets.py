from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  
  # Iteration solution | Time: O(n * 2^n), Space: O(n)
  # def subsets(self, nums: List[int]) -> List[List[int]]:
  #   res = [[]]

  #   for num in nums:
  #     res += [subset + [num] for subset in res]

  #   return res


  # Backtracking solution (best) | Time: O(n * 2^n), Space: O(n)
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i):
      if i >= len(nums):
        res.append(subset.copy())
        return
      subset.append(nums[i])
      dfs(i + 1)
      subset.pop()
      dfs(i + 1)

    dfs(0)
    return res