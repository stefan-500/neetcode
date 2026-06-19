from typing import List
import heapq

"""
Run in the neetcode text editor.
"""
class KthLargest:

  # Sorting solution | Time: O(m), Space: O(1) or O(n) depending on the sorting algorithm,
  # where m is the number of calls made to add(), and n is the current size of the array.
  # def __init__(self, k: int, nums: List[int]):
  #   self.k = k
  #   self.arr = nums

  # def add(self, val: int) -> int:
  #   self.arr.append(val)
  #   self.arr.sort()
  #   return self.arr[len(self.arr) - self.k]
  
  
  # Min Heap solution (best) | Time: O(m * log k), Space: O(k),
  # where m is the number of calls made to add().
  def __init__(self, k: int, nums: List[int]):
    self.minHeap, self.k = nums, k
    heapq.heapify(self.minHeap)
    while len(self.minHeap) > k:
      heapq.heappop(self.minHeap)

  def add(self, val: int) -> int:
    heapq.heappush(self.minHeap, val)
    if len(self.minHeap) > self.k:
      heapq.heappop(self.minHeap)
    return self.minHeap[0]
