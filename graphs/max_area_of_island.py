from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  
  # DFS solution (best) | Time: O(m * n), Space: O(m * n),
  # where m is the number of rows and n is the number of columns in the grid.
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()

    def dfs(r, c):
      if (r < 0 or r == ROWS or c < 0 or
      c == COLS or grid[r][c] == 0 or (r, c) in visit):
        return 0

      visit.add((r, c))
      return (1 + dfs(r + 1, c) +
              dfs(r - 1, c) +
              dfs(r, c + 1) +
              dfs(r, c - 1))

    area = 0
    for r in range(ROWS):
      for c in range(COLS):
        area = max(area, dfs(r, c))
    return area