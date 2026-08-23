"""
Run in the neetcode text editor.
"""
class Solution:

  # Dynamic Programming - Top Down solution | Time: O(n), Space: O(n)
  # def climbStairs(self, n: int) -> int:
  #   cache = [-1] * n
    
  #   def dfs(i):
  #     if i >= n:
  #       return i == n
  #     if cache[i] != -1:
  #       return cache[i]
  #     cache[i] = dfs(i + 1) + dfs(i + 2)
  #     return cache[i]

  #   return dfs(0)


  # Dynamic Programming - Space Optimized solution (best) | Time: O(n), Space: O(1)
  def climbStairs(self, n: int) -> int:
    one, two = 1, 1

    for i in range(n - 1):
      temp = one
      one = one + two
      two = temp

    return one