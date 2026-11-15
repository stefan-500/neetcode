
"""
Run in the neetcode text editor.
"""

class Solution:

  # Memoization solution | Time: O(m * n), Space: O(m * n), where
  # m is the length of the string s and n is the length of the string t.
  def numDistinct(self, s: str, t: str) -> int:
    if len(t) > len(s):
      return 0

    cache = {}
    def dfs(i, j):
      if j == len(t):
        return 1
      if i == len(s):
        return 0
      if (i, j) in cache:
        return cache[(i, j)]

      if s[i] != t[j]:
        cache[(i, j)] = dfs(i + 1, j)
      else:
        cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
      return cache[(i, j)]
        
    return dfs(0, 0)             