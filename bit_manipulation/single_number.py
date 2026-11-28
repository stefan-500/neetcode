from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # Hash Set solution | Time: O(n), Space: O(n)
  # def singleNumber(self, nums: List[int]) -> int:
    
  #   seen = set()
    
  #   for num in nums:
  #     if num in seen:
  #       seen.remove(num)
  #     else:
  #       seen.add(num)
    
  #   return seen.pop()
  

  # Bit manipulation solution (best) | Time: O(n), Space: O(1)
  def singleNumber(self, nums: List[int]) -> int:
    res = 0
    for n in nums:
      res = n ^ res
    
    return res