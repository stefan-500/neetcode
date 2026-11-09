from typing import List

"""
Run in the neetcode text editor.
"""

class Solution:

  # Brute force solution | Time: O(2^n), Space: O(n)
  def findTargetSumWays(self, nums: List[int], target: int) -> int:

    def backtrack(i, total):
      if i == len(nums):
        return  total == target

      return (backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i]))

    return backtrack(0, 0)

  
  # Dynamic programming (top down) solution | Time: O(n * m), Space: O(n * m),
  # where n is the length of the array nums and m is the sum of all the elements in the array.
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    cache = {}

    def backtrack(i, t):
      if i == len(nums):
        return 1 if t == target else 0
      if (i, t) in cache:
        return cache[(i, t)]
      
      cache[(i, t)] = backtrack(i + 1, t + nums[i]) + backtrack(i + 1, t - nums[i])
      return cache[(i, t)]

    return backtrack(0, 0)