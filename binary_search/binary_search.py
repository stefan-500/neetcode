from typing import List
import bisect


# My solution (watched explanation) - redundant
# def search(nums: List[int], target: int) -> int:
#   l = 0
#   r = len(nums) - 1
  
#   while l <= r:
#     mid = (l + r) // 2
#     if nums[mid] != target:
#       if nums[mid] < target:
#         l = mid + 1
#         mid = (l + r) // 2
#       elif nums[mid] > target:
#         r = mid - 1
#         mid = (l + r) // 2
#     else:
#       return mid
#   return -1


# Recursive Binary Search solution | Time: O(n log n), Space: O(n log n)
# def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
#   if l > r:
#     return -1
#   m = l + (r - l) // 2

#   if nums[m] == target:
#     return m
#   if nums[m] < target:
#     return self.binary_search(m + 1, r, nums, target)
#   return self.binary_search(l, m - 1, nums, target)

# def search(self, nums: List[int], target: int) -> int:
#   return self.binary_search(0, len(nums) - 1, nums, target)        


# Upper Bound solution | Time: O(n), Space: O(1)
# def search(nums: List[int], target: int) -> int:
#   l = 0
#   r = len(nums)

#   while l < r:
#     m = l + ((r - l) // 2)
#     if nums[m] > target:
#       r = m
#     elif nums[m] <= target:
#       l = m + 1
#   return l - 1 if (l and nums[l - 1] == target) else -1


# Lower Bound solution | Time: O(n), Space: O(1)
# def search(nums: List[int], target: int) -> int:
#   l = 0
#   r = len(nums)

#   while l < r:
#     m = l + ((r - l) // 2)
#     if nums[m] >= target:
#       r = m
#     elif nums[m] < target:
#       l = m + 1
#   return l if (l < len(nums) and nums[l] == target) else -1


# Built-in function solution | Time: O(n log n), Space: O(1)
# def search(nums: List[int], target: int) -> int:
#   index = bisect.bisect_left(nums, target)
#   return index if index < len(nums) and nums[index] == target else -1


# Binary Search solution (best) | Time: O(n log n), Space: O(1)
def search(nums: List[int], target: int) -> int:
  l = 0
  r = len(nums) - 1

  while l <= r:
    # (l + r) // 2 can lead to overflow (not in Python)
    m = l + ((r - l) // 2)

    if nums[m] > target:
      r = m - 1
    elif nums[m] < target:
      l = m + 1
    else:
      return m
  return -1



nums = [-1, 0, 2, 4, 8]
target = 8
print(search(nums, target))