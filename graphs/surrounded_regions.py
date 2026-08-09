from typing import List

"""
Run in the neetcode text editor.
""" 
class Solution:

  # My solution (explanation and AI help)
  # def solve(self, board: List[List[str]]) -> None:
  #   ROWS, COLS = len(board), len(board[0])
  #   tempCoords = []

  #   def dfs(r, c):
  #     if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != "O":
  #       return

  #     board[r][c] = "T"
  #     tempCoords.append((r, c))
  #     dfs(r + 1, c)
  #     dfs(r - 1, c)
  #     dfs(r, c + 1)
  #     dfs(r, c - 1)

  #   for r in range(ROWS):
  #     for c in range(COLS):
  #       # Mark unsurrounded regions (DFS)
  #       if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
  #         dfs(r, c)

  #   for r in range(ROWS):
  #     for c in range(COLS):
  #       # Capture surrounded regions
  #       if board[r][c] == "O":
  #         board[r][c] = "X"

  #   while tempCoords:
  #     row, col = tempCoords.pop()
  #     # Unmark unsurrounded regions
  #     board[row][col] = "O"


  # DFS solution (best) | Time: O(m * n), Space: O(m * n),
  # where m is the number of rows and n is the number of columns on the board.
  def solve(self, board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
      if (r < 0 or c < 0 or r == ROWS or
        c == COLS or board[r][c] != "O"):
        return

      board[r][c] = "T"
      capture(r + 1, c)
      capture(r - 1, c)
      capture(r, c + 1)
      capture(r, c - 1)

    for r in range(ROWS):
      if board[r][0] == "O":
        capture(r, 0)
      if board[r][COLS - 1] == "O":
        capture(r, COLS - 1)
    
    for c in range(COLS):
      if board[0][c] == "O":
        capture(0, c)
      if board[ROWS - 1][c] == "O":
        capture(ROWS - 1, c)

    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] == "O":
          board[r][c] = "X"
        elif board[r][c] == "T":
          board[r][c] = "O"