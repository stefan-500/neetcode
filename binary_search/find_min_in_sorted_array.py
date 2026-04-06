from typing import List


# Brute Force solution | Time: O(n), Space: O(1)
# def findMin(nums: List[int]) -> int:
#   return min(nums)


# Binary Search solution (best) | Time: O(log n), Space: O(1)
def findMin(nums: List[int]) -> int:
  res = nums[0]
  l = 0
  r = len(nums) - 1

  while l <= r:
    if nums[l] < nums[r]:
      res = min(res, nums[l])
      break
    
    m = (l + r) // 2
    res = min(res, nums[m])
    if nums[m] >= nums[l]:
      l = m + 1
    else:
      r = m - 1
  return res



nums = [3,4,5,6,1,2]
print(findMin(nums))