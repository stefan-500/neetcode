from typing import List


# Brute Force solution | Time: O(n), Space: O(1)
# def search(nums: List[int], target: int) -> int:
#   for i in range(len(nums)):
#     if nums[i] == target:
#       return i
#   return -1


# Binary Search (One Pass) solution (best) | Time: O(log n), Space: O(1)
def search(nums: List[int], target: int) -> int:
  l = 0
  r = len(nums) - 1

  while l <= r:
    mid = (l + r) // 2
    if target == nums[mid]:
      return mid

    if nums[l] <= nums[mid]:
      if target > nums[mid] or target < nums[l]:
        l = mid + 1
      else:
        r = mid - 1
    else:
      if target < nums[mid] or target > nums[r]:
        r = mid - 1
      else:
        l = mid + 1
  return -1



nums=[4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))