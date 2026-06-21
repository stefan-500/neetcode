from typing import List
import heapq

"""
Run in the neetcode text editor.
"""
class Solution:

  # My solution
  # def lastStoneWeight(self, stones: List[int]) -> int:
  #   stones = sorted(stones, reverse=True)
  #   while len(stones) > 1:
  #     x = stones[0]
  #     y = stones[1]
  #     if x == y:
  #       stones = stones[2:]
  #     elif x < y:
  #       stones[1] = y - x
  #       stones = stones[1:]
  #     else:
  #       stones[0] = x - y
  #       stones[1] = stones[0]
  #       stones = stones[1:]
  #     stones = sorted(stones, reverse=True)
                
  #   return stones[0] if stones else 0


  # Max Heap solution (best) | Time: O(n log n), Space: O(n)
  def lastStoneWeight(self, stones: List[int]) -> int:      
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
      first = heapq.heappop(stones)
      second = heapq.heappop(stones)
      if second > first:
        heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])