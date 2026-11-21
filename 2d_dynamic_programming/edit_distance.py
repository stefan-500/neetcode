"""
Run in the neetcode text editor.
"""

class Solution:
  
  # Brute force solution
  # def minDistance(self, word1: str, word2: str) -> int:
    
  #   def dfs(i, j):
  #     if i == len(word1):
  #       return len(word2) - j

  #     if j == len(word2):
  #       return len(word1) - i

  #     if word2[j] == word1[i]:
  #       return dfs(i + 1, j + 1)
  #     else:
  #       # insert, replace, or delete
  #       return 1 + min(dfs(i, j + 1), dfs(i + 1, j + 1), dfs(i + 1, j))

  #   return dfs(0, 0)


  # Memoization solution | Time: O(m * n), Space: O(m * n),
  # where m is the length of word1 and n is the length of word2.
  def minDistance(self, word1: str, word2: str) -> int:
    
    cache = {}
    def dfs(i, j):
      if i == len(word1):
        return len(word2) - j

      if j == len(word2):
        return len(word1) - i

      if (i, j) in cache:
        return cache[(i, j)]

      if word2[j] == word1[i]:
        return dfs(i + 1, j + 1)
      else:
        # insert, replace, or delete
        cache[(i, j)] = 1 + min(dfs(i, j + 1), 
                                dfs(i + 1, j + 1), 
                                dfs(i + 1, j))        
        return cache[(i, j)]

    return dfs(0, 0)