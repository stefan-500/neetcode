from typing import List
import heapq

"""
Run in the neetcode text editor.
"""
class Solution:

  # Sorting solution | Time: O(n log n), Space: O(1) or O(1) depending on the sorting algorithm.
  # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
  #   points.sort(key = lambda p: p[0]**2 + p[1]**2)
  #   return points[:k]


  # Max Heap solution | Time: O(n * log k), Space: O(k) where n is the length of the array points.
  # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
  #   maxHeap = []
  #   for x, y in points:
  #     dist = -(x ** 2 + y ** 2)
  #     heapq.heappush(maxHeap, [dist, x, y])
  #     if len(maxHeap) > k:
  #       heapq.heappop(maxHeap)

  #   res = []
  #   while maxHeap:
  #     dist, x, y = heapq.heappop(maxHeap)
  #     res.append([x, y])
  #   return res


  # Min Heap solution (best) | Time: O(n + k * log n), when building the heap with heapify,
  # or O(n * log n + k * log n) when inserting each point with a heap push, Space: O(n)
  # where n is the length of the array points.
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []
    for x, y in points:
      dist = (x ** 2) + (y ** 2)
      minHeap.append([dist, x, y])

    heapq.heapify(minHeap)
    res = []
    while k:
      dist, x, y = heapq.heappop(minHeap)
      res.append([x, y])
      k -= 1
    return res