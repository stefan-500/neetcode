from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # Dynamic Programming solution (best) | Time: O(n * target), Space: O(target),
  # where n is the length of the array nums and target is the sum of array
  # elements divided by 2.
  def canPartition(self, nums: List[int]) -> bool:
    if sum(nums) % 2:
      return False

    dp = set()
    dp.add(0)
    target = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
      nextDP = set()
      for t in dp:
        if (t + nums[i] == target):
          return True
        nextDP.add(t + nums[i])
        nextDP.add(t)
      dp = nextDP
    return False