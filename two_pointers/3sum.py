from typing import List
from collections import defaultdict

# My solution, ChatGPT helped
# def threeSum(nums: List[int]) -> List[List[int]]:
#   resMap = {}   # dictionary ignores duplicate key appending
#   if not nums:
#     return []
  
#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       for k in range(len(nums)):
#         if (k == i or k == j):  # ignore the current i and j observations
#           continue
#         if nums[i] + nums[j] + nums[k] == 0:
#           tripletKey = ''.join(str(x) for x in sorted([nums[i], nums[j], nums[k]]))   # e.g. '-202', for assuring no duplicate triplets
#           resMap[tripletKey] = [nums[i], nums[j], nums[k]]
#   return list(resMap.values())


# Brute Force solution | Time: O(n^3), Space: O(m), where m is the number of triplets
# def threeSum(nums: List[int]) -> List[List[int]]:
#   res = set()
#   nums.sort()
#   for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#       for k in range(j + 1, len(nums)):
#         if nums[i] + nums[j] + nums[k] == 0:
#           tmp = [nums[i], nums[j], nums[k]]
#           res.add(tuple(tmp))
#   return [list(i) for i in res]


# Hash Map solution | Time: O(n^2), Space: O(n)
# def threeSum(nums: List[int]) -> List[List[int]]:
#   nums.sort()
#   count = defaultdict(int)
#   for num in nums:
#     count[num] += 1
  
#   res = []
#   for i in range(len(nums)):
#     count[nums[i]] -= 1
#     if i and nums[i] == nums[i - 1]:
#       continue
    
#     for j in range(i + 1, len(nums)):
#       count[nums[j]] -= 1
#       if j - 1 > i and nums[j] == nums[j - 1]:
#         continue
#       target = -(nums[i] + nums[j])
#       if count[target] > 0:
#         res.append([nums[i], nums[j], target])
    
#     for j in range(i + 1, len(nums)):
#       count[nums[j]] += 1
#   return res


# Two Pointers solution (best) | Time: O(n^2), Space: O(1) or O(n)
def threeSum(nums: List[int]) -> List[List[int]]:
  res = []
  nums.sort()

  for i, a in enumerate(nums):
    if a > 0:   # remaining numbers are all positive
      break

    if i > 0 and a == nums[i - 1]:    # ignore duplicates
      continue

    l, r = i + 1, len(nums) - 1
    while l < r:
      threeSum = a + nums[l] + nums[r]
      
      if threeSum > 0:
        r -= 1
      elif threeSum < 0:
        l += 1
      else:
        res.append([a, nums[l], nums[r]])
        l += 1
        r -= 1
        while nums[l] == nums[l - 1] and l < r:   # ignore duplicates
          l += 1

  return res



nums = [-2, 0, 5, 2, -4, 10, -1, 6]
print(threeSum(nums))