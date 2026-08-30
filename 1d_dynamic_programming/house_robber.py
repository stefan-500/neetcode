from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # Brute Force solution | Time: O(2^n), Space: O(n)
  # def rob(self, nums: List[int]) -> int:
  #   def dfs(i):
  #     if i >= len(nums):
  #       return 0
  #     return max(dfs(i + 1), nums[i] + dfs(i + 2))
    
  #   return dfs(0)


  # Dynamic Programming solution (best) | Time: O(n), Space: O(1)
  def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
      temp = max(n + rob1, rob2)
      rob1 = rob2
      rob2 = temp
    
    return rob2