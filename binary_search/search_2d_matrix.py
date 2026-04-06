from typing import List


# My solution
# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#   mat = []
#   for i in matrix:
#     for j in i:
#       mat.append(j)

#   l = 0
#   r = len(mat) - 1
#   while l <= r:
#     # mid = (l + r) // 2
#     mid = l + ((r - l) // 2)
#     if mat[mid] < target:
#       l = mid + 1
#     elif mat[mid] > target:
#       r = mid - 1
#     else:
#       return True
#   return False


# My 2. solution
# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#   n = len(matrix)
#   for row in range(len(matrix)):
#     if matrix[row][-1] < target:    # skip unnecessary rows
#       continue    
    
#     l, r = 0, len(matrix[row]) - 1
#     while l <= r:
#       mid = l + ((r - l) // 2)
#       if matrix[row][mid] < target:
#         l = mid + 1
#       elif matrix[row][mid] > target:
#         r = mid - 1
#       else:
#         return True
#   return False


# Brute Force solution | Time: O(m * n), Space: O(1)
# def searchMatrix(matrix: List[List[int]], target: int) -> bool:        
#   for r in range(len(matrix)):
#     for c in range(len(matrix[0])):
#       if matrix[r][c] == target:
#         return True
#   return False


# Binary Search solution (best) | Time: O(log (m * n)), Space: O(1),
# where m = number of rows and n = number of cols in matrix
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
  ROWS = len(matrix)
  COLS = len(matrix[0])

  top = 0
  bot = ROWS - 1
  while top <= bot:
    row = (top + bot) // 2
    if target > matrix[row][-1]:
        top = row + 1
    elif target < matrix[row][0]:
        bot = row - 1
    else:
        break

  if not (top <= bot):    # no potential row found
    return False

  row = (top + bot) // 2
  l = 0
  r = COLS - 1
  while l <= r:
    m = (l + r) // 2
    if target > matrix[row][m]:
        l = m + 1
    elif target < matrix[row][m]:
        r = m - 1
    else:
        return True
  return False



matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 20
print(searchMatrix(matrix, target))