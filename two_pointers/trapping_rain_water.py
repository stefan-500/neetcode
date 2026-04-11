from typing import List


# Brute Force solution | Time: O(n^2), Space: O(1)
# def trap(height: List[int]) -> int:
#   if not height:
#     return 0
#   n = len(height)
#   res = 0

#   for i in range(n):
#     leftMax = height[i]
#     rightMax = height[i]

#     for j in range(i):
#       leftMax = max(leftMax, height[j])
#     for j in range(i + 1, n):
#       rightMax = max(rightMax, height[j])

#     res += min(leftMax, rightMax) - height[i]
#   return res


# Prefix & Suffix Arrays solution | Time: O(n), Space: O(n)
# def trap(height: List[int]) -> int:
#   n = len(height)
#   if n == 0:
#     return 0
  
#   leftMax = [0] * n
#   rightMax = [0] * n

#   leftMax[0] = height[0]
#   for i in range(1, n):
#     leftMax[i] = max(leftMax[i - 1], height[i])
  
#   rightMax[n - 1] = height[n - 1]
#   for i in range(n - 2, -1, -1):
#     rightMax[i] = max(rightMax[i + 1], height[i])
  
#   res = 0
#   for i in range(n):
#     res += min(leftMax[i], rightMax[i]) - height[i]
#   return res


# Stack solution | Time: O(n), Space: O(n)
# def trap(height: List[int]) -> int:
#   if not height:
#     return 0
#   stack = []
#   res = 0

#   for i in range(len(height)):
#     while stack and height[i] >= height[stack[-1]]:
#       mid = height[stack.pop()]
#       if stack:
#         right = height[i]
#         left = height[stack[-1]]
#         h = min(right, left) - mid
#         w = i - stack[-1] - 1
#         res += h * w
#     stack.append(i)
#   return res


# Two Pointers solution (best) | Time: O(n), Space: O(1)
def trap(height: List[int]) -> int:
  if not height:
    return 0
  
  l = 0
  r = len(height) - 1
  leftMax = height[l]
  rightMax = height[r]
  res = 0
  
  while l < r:
    if leftMax < rightMax:
      l += 1
      leftMax = max(leftMax, height[l])
      res += leftMax - height[l]
    else:
      r -= 1
      rightMax = max(rightMax, height[r])
      res += rightMax - height[r]
  return res



height=[4,2,0,3,2,5]
print(trap(height))