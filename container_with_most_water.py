from typing import List

# My solution (seen the brute force solution)
# def maxArea(heights: List[int]) -> int:
#   res = w = h = 0
  
#   for i in range(len(heights)):  
#     for j in range(len(heights) - 1, -1, -1):
#       w = j - i
#       h = min(heights[j], heights[i])   # smaller bar is the edge
#       res = max(res, (w * h))   # amount of water = width * height of container
#   return res
  

# Brute force solution | Time: O(n^2), Space: O(1)
# def maxArea(heights: List[int]) -> int:
#   res = 0
#   for i in range(len(heights)):
#     for j in range(i + 1, len(heights)):
#       res = max(res, min(heights[i], heights[j]) * (j - i))
#   return res


# Two Pointers solution (best) | Time: O(n), Space: O(1)
def maxArea(heights: List[int]) -> int:
  l = 0
  r = len(heights) - 1
  res = 0

  while l < r:
    area = min(heights[l], heights[r]) * (r - l)    # smaller line * width
    res = max(res, area)
    if heights[l] <= heights[r]:
      l += 1
    else:
      r -= 1
  return res



heights = [1,7,2,5,4,7,3,6]
print(maxArea(heights))
