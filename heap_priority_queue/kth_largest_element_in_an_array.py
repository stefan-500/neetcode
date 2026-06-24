from typing import List
import heapq

"""
Run in the neetcode text editor.
"""
class Solution:

  # My 1. solution
  # def findKthLargest(self, nums: List[int], k: int) -> int:
  #   n = sorted(nums, reverse=True)
  #   while k > 1:
  #     n.pop(0)
  #     k -= 1
  #   return n.pop(0)
  

  # My 2. solution (mostly copied from kth_largest_element_in_a_stream.py)
  # def findKthLargest(self, nums: List[int], k: int) -> int:
  #   heapq.heapify(nums)
  #   while len(nums) > k:
  #     heapq.heappop(nums)  
  #   return nums[0]


  # Min Heap solution (best) | Time: O(n log k) | Space: O(k)
  # where n is the length of the array nums.
  def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
