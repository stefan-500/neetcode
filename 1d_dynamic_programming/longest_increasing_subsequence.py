from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # Dynamic Programming - Bottom up solution (best) | Time: O(n^2), Space: O(n) 
  def lengthOfLIS(self, nums: List[int]) -> int:
    LIS = [1] * len(nums)
    
    for i in range(len(nums) - 1, -1, -1):
      for j in range(i + 1, len(nums)):
        if nums[i] < nums[j]:
          LIS[i] = max(LIS[i], 1 + LIS[j])
        
    return max(LIS)