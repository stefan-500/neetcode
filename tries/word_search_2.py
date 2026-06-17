from typing import List

"""
Run in the neetcode text editor.
"""

# Backtracking (Trie and Hash Set) solution (best) | Time: O(M * n * 4 * 3^(t-1) + 8), Space: O(s),
# where M is the number of rows, n is the number of the columns, t is the maximum length of any word
# in the array words, and s is the sum of the lengths of all the words.
class TrieNode:
  def __init__(self):
    self.children = {}
    self.isWord = False

  def addWord(self, word):
    cur = self
    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.isWord = True

class Solution:
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    root = TrieNode()
    for w in words:
      root.addWord(w)

    ROWS, COLS = len(board), len(board[0])
    res, visit = set(), set()

    def dfs(r, c, node, word):
      if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or board[r][c] not in node.children):
        return

      visit.add((r, c))
      node = node.children[board[r][c]]
      word += board[r][c]
      if node.isWord:
        res.add(word)

      dfs(r + 1, c, node, word)
      dfs(r - 1, c, node, word)
      dfs(r, c + 1, node, word)
      dfs(r, c - 1, node, word)
      visit.remove((r, c))

    for r in range(ROWS):
      for c in range(COLS):
        dfs(r, c, root, "")

    return list(res)