from typing import List
from collections import defaultdict


# My solution
# def twoSum(numbers: List[int], target: int) -> List[int]:
#   for i in range(len(numbers)):
#     if numbers[i] > abs(target):
#       continue

#     for j in range(i + 1, len(numbers)):
#       if (numbers[i] + numbers[j]) == target:
#         return [i+1, j+1]


# Brute force solution | Time: O(n^2), Space: O(1)
# def twoSum(numbers: List[int], target: int) -> List[int]:
#   for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#       if numbers[i] + numbers[j] == target:
#         return [i + 1, j + 1]
#   return []


# Binary search solution | Time: O(n log n), Space: O(1)
# def twoSum(numbers: List[int], target: int) -> List[int]:
#   for i in range(len(numbers)):
#     l = i + 1
#     r = len(numbers) - 1
#     tmp = target - numbers[i]

#     while l <= r:
#       mid = l + (r - l) // 2

#       if numbers[mid] == tmp:
#         return [i + 1, mid + 1]
#       elif numbers[mid] < tmp:
#         l = mid + 1
#       else:
#         r = mid - 1
#   return []


# Hash map solution | Time: O(n), Space: O(n)
# def twoSum(numbers: List[int], target: int) -> List[int]:  
#   mp = defaultdict(int)
#   for i in range(len(numbers)):
#     tmp = target - numbers[i]
#     if mp[tmp]:
#       return[mp[tmp], i + 1]
#     mp[numbers[i]] = i + 1
#   return []


# Two pointers solution (best) | Time: O(n), Space: O(1)
def twoSum(numbers: List[int], target: int) -> List[int]:
  l = 0
  r = len(numbers) - 1

  while l < r:
    curSum = numbers[l] + numbers[r]

    if curSum > target:
      r -= 1
    elif curSum < target:
      l += 1
    else:
      return [l + 1, r + 1]
  return []



numbers = [1, 3, 4, 5, 7, 11]
target = 9
print(twoSum(numbers, target))