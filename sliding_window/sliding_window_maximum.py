from typing import List
from collections import deque

# My solution (ChatGPT helped)
# def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
#   l = 0
#   r = k - 1
#   res = []
  
#   while r <= len(nums) - 1:
#     currMax = max(nums[l : r + 1])
#     res.append(currMax)  
#     l += 1
#     r += 1
#   return res


# Brute Force solution | Time: O(n * k), Space: O(1), 
# O(n - k + 1) space for the output array, where
# n is the length of the array and k is the size of the window.
# def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
#   output = []

#   for i in range(len(nums) - k + 1):
#     maxi = nums[i]
#     for j in range(i, i + k):
#       maxi = max(maxi, nums[j])
    
#     output.append(maxi)
#   return output


# Deque solution (best) | Time: O(n), Space: O(n)
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
  output = []
  q = deque() # index
  l = 0
  r = 0

  while r < len(nums):
    while q and nums[q[-1]] < nums[r]:
        q.pop()
    q.append(r)

    if l > q[0]:
        q.popleft()
    
    if (r + 1) >= k:
        output.append(nums[q[0]])
        l += 1
    r += 1

  return output



nums = [1,2,1,0,4,2,6]
k = 3
print(maxSlidingWindow(nums, k))