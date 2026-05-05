from typing import List


# My solution
# def findDuplicate(nums: List[int]) -> int:
#   nums = sorted(nums)
#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       if nums[j] == nums[i]:
#         return nums[i]
#       break


# My 2. solution (without modifying nums)
# def findDuplicate(nums: List[int]) -> int:
#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       if nums[j] == nums[i]:
#         return nums[i]


# Sorting solution | Time: O(n log n), Space: O(1) or O(n)
# def findDuplicate(nums: List[int]) -> int:
#   nums.sort()
#   for i in range(len(nums) - 1):
#     if nums[i] == nums[i + 1]:
#       return nums[i]
#   return -1


# Hash Set solution | Time: O(n), Space: O(n)
# def findDuplicate(nums: List[int]) -> int:
#   seen = set()
#   for num in nums:
#     if num in seen:
#       return num
#     seen.add(num)
#   return -1


# Array solution | Time: O(n), Space: O(n)
# def findDuplicate(nums: List[int]) -> int:
#   seen = [0] * len(nums)
#   for num in nums:
#     if seen[num - 1]:
#       return num
#     seen[num - 1] = 1
#   return -1


# Fast and Slow Pointers solution (best) | Time: O(n), Space: O(1)
def findDuplicate(nums: List[int]) -> int:
  slow = 0
  fast = 0
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
      break
  
  slow2 = 0
  while True:
    slow = nums[slow]
    slow2 = nums[slow2]
    if slow == slow2:
      return slow



nums = [1,2,3,4,4]
print(findDuplicate(nums))