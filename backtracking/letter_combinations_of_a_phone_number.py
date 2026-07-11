from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:
  
  # Iteration solution | Time: O(n * 4^n), Space: O(n)
  # def letterCombinations(self, digits: str) -> List[str]:
  #   if not digits:
  #     return []

  #   res = [""]
  #   digitToChar = {
  #     "2": "abc",
  #     "3": "def",
  #     "4": "ghi",
  #     "5": "jkl",
  #     "6": "mno",
  #     "7": "qprs",
  #     "8": "tuv",
  #     "9": "wxyz",
  #   }

  #   for digit in digits:
  #     tmp = []
  #     for curStr in res:
  #       for c in digitToChar[digit]:
  #         tmp.append(curStr + c)
  #     res = tmp
  #   return res 
  
  
  # Backtracking solution (best) | Time: O(n * 4^n), Space: O(n)
  def letterCombinations(self, digits: str) -> List[str]:
    res = []
    digitToChar = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
    "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]}

    def backtrack(i, curStr):
      if len(curStr) == len(digits):
        res.append(curStr)
        return

      for c in digitToChar[digits[i]]:
        backtrack(i + 1, curStr + c)

    if digits:
      backtrack(0, "")
    
    return res