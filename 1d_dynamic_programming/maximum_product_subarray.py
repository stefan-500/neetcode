from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # Brute Force solution | Time: O(n^2)
  # def maxProduct(self, nums: List[int]) -> int:
  #   prods = []

  #   for i in range(len(nums)):
  #     curProd = 1

  #     for j in range(i, len(nums)):
  #       curProd *= nums[j]
  #       prods.append(curProd)

  #   return max(prods)
  
  
  # Kadane's algorithm solution (best) | Time: O(n), Space: O(1)
  def maxProduct(self, nums: List[int]) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for num in nums:
      tmp = curMax * num
      curMax = max(num * curMax, num * curMin, num)
      curMin = min(tmp, num * curMin, num)
      res = max(res, curMax)
    return res