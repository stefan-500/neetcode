"""
Run in the neetcode text editor.
"""

class Solution:
  
  # Brute Force Solution | Time: O(2^(m + n)), Space: O(m + n),
  # where m is the number of rows and n is the number of columns.
  # def uniquePaths(self, m: int, n: int) -> int:
  #   def dfs(i, j):
  #     if i == (m - 1) and j == (n - 1):
  #       return 1
  #     if i == m or j == n:
  #       return 0

  #     return dfs(i + 1, j) + dfs(i, j + 1)
  
  #   return dfs(0, 0)


  # Optimized Dynamic Programming Solution (best) | Time: O(m * n), Space: O(n)
  def uniquePaths(self, m: int, n: int) -> int:
    row = [1] * n

    for i in range(m - 1):
      newRow = [1] * n
      for j in range(n - 2, -1, -1):
        newRow[j] = newRow[j + 1] + row[j]
      row = newRow
    return row[0]