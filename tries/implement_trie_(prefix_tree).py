"""
Run in the neetcode text editor.
"""

# Prefix Tree (Array) | Time: O(n) for each function call, Space: O(t),
# where n is the length of the string and t
# is the total number of TrieNodes created in the Trie
# class TrieNode:
#   def __init__(self):
#     self.children = [None] * 26
#     self.endOfWord = False

# class PrefixTree:

#   def __init__(self):
#     self.root = TrieNode()        

#   def insert(self, word: str) -> None:
#     cur = self.root
#     for c in word:
#       i = ord(c) - ord("a")
#       if cur.children[i] == None:
#         cur.children[i] = TrieNode()
#       cur = cur.children[i]
#     cur.endOfWord = True

#   def search(self, word: str) -> bool:
#     cur = self.root
#     for c in word:
#       i = ord(c) - ord("a")
#       if cur.children[i] == None:
#         return False
#       cur = cur.children[i]
#     return cur.endOfWord

#   def startsWith(self, prefix: str) -> bool:
#     cur = self.root
#     for c in prefix:
#       i = ord(c) - ord("a")
#       if cur.children[i] == None:
#         return False
#       cur = cur.children[i]
#     return True


# Prefix Tree (Hash Map) (best) | Time: O(n) for each function call, Space: O(t),
# where n is the length of the string and t
# is the total number of TrieNodes created in the Trie
class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfWord = False

class PrefixTree:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    cur = self.root

    for c in word:
      if c not in cur.children:
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.endOfWord = True

  def search(self, word: str) -> bool:
    cur = self.root

    for c in word:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return cur.endOfWord

  def startsWith(self, prefix: str) -> bool:
    cur = self.root

    for c in prefix:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    return True
    