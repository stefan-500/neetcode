from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  
  # DFS solution (best) | Time: O(m * n), Space: O(m * n),
  # where m is the number of rows and n is the number of columns in the grid.
  # One DFS call removes one whole island,
  # the outer loops count how many times a new DFS must be started.
  def numIslands(self, grid: List[List[str]]) -> int:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ROWS, COLS = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
      # Return if outside of grid or at '0'
      if (r < 0 or c < 0 or r >= ROWS or
        c >= COLS or grid[r][c] == "0"):
        return

      # Mark cell as water (visited)
      grid[r][c] = "0"

      for dr, dc in directions:
        dfs(r + dr, c + dc)

    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == "1":
          dfs(r, c)
          islands += 1
    
    return islands