from typing import List
from collections import defaultdict


# My solution (ChatGPT helped)
# def isValidSudoku(board: List[List[str]]) -> bool:
#   seen = set()
#   # Row handling
#   for row in board:
#     # Init clean list for every row
#     seen.clear()
#     for i in range(9):
#       if not row[i].isdigit():  # ignore non-digit cells
#         continue

#       if row[i] in seen:
#         return False
#       seen.add(row[i])

#   # Column handling
#   for col in zip(*board):
#     seen.clear()    
#     for i in range(9):
#       if not col[i].isdigit():
#         continue

#       if col[i] in seen:
#         return False
#       seen.add(col[i])
    
#   # Sub-box handling
#   subboxes = []
#   for row in range(0, 9, 3):
#     for col in range(0, 9, 3):
#       subbox = [board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]
#       subboxes.append(subbox)

#   for sb in subboxes:
#     seen.clear()
#     for i in range(9):
#       if not sb[i].isdigit():
#         continue

#       if sb[i] in seen:
#         return False
#       seen.add(sb[i])

#   return True


# Brute Force solution | Time: O(n^2), Space: O(n)
# def isValidSudoku(board: List[List[str]]) -> bool:
#   for row in range(9):
#     seen = set()

#     for i in range(9):
#       if board[row][i] == ".":
#         continue
#       if board[row][i] in seen:
#         return False
#       seen.add(board[row][i])

#   for col in range(9):
#     seen = set()
    
#     for i in range(9):
#       if board[i][col] == ".":
#         continue
#       if board[i][col] in seen:
#         return False
#       seen.add(board[i][col])

#   for square in range(9):
#     seen = set()
    
#     for i in range(3):
#       for j in range(3):
#         row = (square // 3) * 3 + i
#         col = (square % 3) * 3 + j
        
#         if board[row][col] == ".":
#           continue
        
#         if board[row][col] in seen:
#           return False
#         seen.add(board[row][col])
#   return True


# Bit Mask solution | Time: O(n^2), Space: O(n)
# def isValidSudoku(board: List[List[str]]) -> bool:
#   rows = [0] * 9
#   cols = [0] * 9
#   squares = [0] * 9

#   for r in range(9):
#     for c in range(9):
#       if board[r][c] == ".":
#         continue
      
#       val = int(board[r][c]) - 1  # convert to a bit index
#       if (1 << val) & rows[r]:
#           return False
#       if (1 << val) & cols[c]:
#           return False
#       if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
#           return False
      
#       rows[r] |= (1 << val)
#       cols[c] |= (1 << val)
#       squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

#   return True


# Hash Set solution (best) | Time: O(n^2), Space: O(n^2)
def isValidSudoku(board: List[List[str]]) -> bool:
  rows = defaultdict(set)
  cols = defaultdict(set)
  subboxes = defaultdict(set)

  for r in range(9):
    for c in range(9):
      if board[r][c] == ".":
        continue
      
      if (board[r][c] in rows[r] 
          or board[r][c] in cols[c] 
          or board[r][c] in subboxes[(r // 3, c // 3)]):
        return False

      rows[r].add(board[r][c])
      cols[c].add(board[r][c])
      subboxes[(r // 3, c // 3)].add(board[r][c])

  return True



board = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))