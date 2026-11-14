"""
Run in the neetcode text editor.
"""

class Solution:

  # Caching solution (AI helped)
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    cache = {}
    def dfs(i, j):
      k = i + j
      if k == len(s3):
        return True
      if (i, j) in cache:
        return cache[(i, j)]

      if (i < len(s1) and j < len(s2) and (s3[k] == s1[i]) and (s3[k] == s2[j])):
        cache[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
      elif i < len(s1) and s3[k] == s1[i]:
        cache[(i, j)] = dfs(i + 1, j)
      elif j < len(s2) and s3[k] == s2[j]:
        cache[(i, j)] = dfs(i, j + 1)
      else:
        cache[(i, j)] = False

      return cache[(i, j)]

    return dfs(0, 0)