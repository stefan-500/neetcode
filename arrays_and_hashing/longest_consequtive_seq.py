from typing import List
from collections import defaultdict


# My solution
# def longestConsecutive(nums: List[int]) -> int:
#   seq = []
#   sequences = defaultdict(int)
#   nums = sorted(nums)

#   if not nums:
#     return 0
  
#   # print(f"nums: {nums}\n")
#   for n in range(len(nums)):  
#     if n == 0:
#       seq.append(nums[n])
#       continue
    
#     if n > 0:
#       if nums[n] - nums[n - 1] > 1:
#         sequences[len(seq)] = seq
#         seq.clear()
#         seq.append(nums[n])
#         continue
    
#     if nums[n] - nums[n - 1] == 1:  # if cur is +1 than prev
#       seq.append(nums[n])
#       # print(seq)

#   sequences[len(seq)] = seq
#   return max(sequences)


# Brute Force solution | Time: O(n^2), Space: O(n)
# def longestConsecutive(nums: List[int]) -> int:
#   res = 0
#   store = set(nums)

#   for num in nums:
#     streak = 0
#     curr = num
#     while curr in store:
#       streak += 1
#       curr += 1
#     res = max(res, streak)
#   return res


# Sorting solution | Time: O(n log n), Space: O(1) / O(n)
# def longestConsecutive(nums: List[int]) -> int:
#   if not nums:
#     return 0
#   res = 0
#   nums.sort()

#   curr = nums[0]
#   streak = 0
#   i = 0
#   while i < len(nums):
#     if curr != nums[i]:
#       curr = nums[i]
#       streak = 0
#     while i < len(nums) and nums[i] == curr:
#       i += 1
#     streak += 1
#     curr += 1
#     res = max(res, streak)
#   return res


# Hash Map solution | Time: O(n), Space: O(n)
# def longestConsecutive(nums: List[int]) -> int:
#   mp = defaultdict(int)
#   res = 0

#   for num in nums:
#     if not mp[num]:
#       mp[num] = mp[num - 1] + mp[num + 1] + 1
#       mp[num - mp[num - 1]] = mp[num] 
#       mp[num + mp[num + 1]] = mp[num] 
#       res = max(res, mp[num])
#   return res


# Hash Set solution (best) | Time: O(n), Space: O(n)
def longestConsecutive(nums: List[int]) -> int:
  numSet = set(nums)
  longest = 0

  for num in numSet:
    if (num - 1) not in numSet:
      length = 1
      while (num + length) in numSet:
        length += 1
      longest = max(length, longest)
  return longest



nums = [2, 20, 4, 10, 3, 4, 5]
print(longestConsecutive(nums))