from typing import List
import math


# Brute Force solution | Time: O(m * n), Space: O(1),
# where n is the piles array length and m is the maximum number in the piles array.
# def minEatingSpeed(piles: List[int], h: int) -> int:
#   speed = 1
#   while True:
#     totalTime = 0
#     for pile in piles:
#       totalTime += math.ceil(pile / speed)

#     if totalTime <= h:
#       return speed
#     speed += 1
#   return speed


# Binary Search solution (best) | Time: O(n * log m), Space: O(1), 
# where n is the piles array length and m is the maximum number in the piles array.
def minEatingSpeed(piles: List[int], h: int) -> int:
  l = 1
  r = max(piles)
  res = r

  while l <= r:
    k = (l + r) // 2    
    totalTime = 0
    for p in piles:
      totalTime += math.ceil(float(p) / k)

    if totalTime <= h:
      res = k
      r = k - 1
    else:
      l = k + 1
  return res



piles = [3, 6, 7, 11]
h = 9
print(minEatingSpeed(piles, h))