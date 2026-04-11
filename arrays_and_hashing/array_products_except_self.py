from typing import List
import math 

# My solution | O(n^2)
# def productExceptSelf(nums: List[int]) -> List[int]:
#   res = []
#   i = 0

#   print(f"nums: {nums}\n")
#   for i in range(len(nums)):
#     pref = nums[:i]
#     suf = nums[i+1:]
#     print(f"{'-'*10} current: {nums[i]} {'-'*10}")
#     print(f"Prefix: {pref}")
#     print(f"Suffix: {suf}")
#     product = math.prod(pref) * math.prod(suf)
#     print(f"Arrays product: {product}")
#     res.append(product)
#     print(f"Result: {res}")
#     print("\n")

#   return res


# Brute Force solution  |  Time: O(n^2)
# def productExceptSelf(nums: List[int]) -> List[int]:
#   n = len(nums)
#   res = [0] * n

#   for i in range(n):
#     prod = 1
#     for j in range(n):
#       if i == j:
#         continue
#       prod *= nums[j]

#     res[i] = prod
#   return res


# Division solution  |  Time: O(n)
# def productExceptSelf(nums: List[int]) -> List[int]:
  # prod, zero_cnt = 1, 0
  # for num in nums:
  #   if num:
  #     prod *= num
  #   else:
  #     zero_cnt += 1
  # if zero_cnt > 1:
  #   return [0] * len(nums)

  # res = [0] * len(nums)
  # for i, c in enumerate(nums):
  #   if zero_cnt: 
  #     res[i] = 0 if c else prod
  #   else:
  #     res[i] = prod // c
  
  # return res


# Prefix & Suffix solution without redundant multiplication  |  Time: O(n), Space: O(n)
# def productExceptSelf(nums: List[int]) -> List[int]:
#   n = len(nums)
#   res = [0] * n
#   pref = [0] * n
#   suff = [0] * n

#   pref[0] = 1
#   suff[n - 1] = 1
#   for i in range(1, n):
#     pref[i] = nums[i - 1] * pref[i - 1]

#   for i in range(n - 2, -1, -1):
#     suff[i] = nums[i + 1] * suff[i + 1]

#   for i in range(n):
#     res[i] = pref[i] * suff[i]
#   return res


# Best solution  |  Time: O(n), Space: O(1)
def productExceptSelf(nums: List[int]) -> List[int]:
  res = [1] * (len(nums))

  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

  postfix = 1
  for i in range(len(nums) - 1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]

  return res


arr = [1, 2, 4, 6]
print(productExceptSelf(arr))