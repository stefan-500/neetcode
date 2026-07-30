from typing import List
from collections import deque

"""
Run in the neetcode text editor.
"""
class Solution:
  # Multi source BFS solution (best) | Time: O(m * n), Space: O(m * n),
  # where m is the number of rows and n is the number of columns in the grid.
  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    q = deque()

    def addCell(r, c):
      if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
        return
      visit.add((r, c))
      q.append([r, c])

    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 0:
          q.append([r, c])
          visit.add((r, c))
    
    dist = 0
    while q:
      for i in range(len(q)):
          r, c = q.popleft()
          grid[r][c] = dist
          addCell(r + 1, c)
          addCell(r - 1, c)
          addCell(r, c + 1)
          addCell(r, c - 1)
      dist += 1