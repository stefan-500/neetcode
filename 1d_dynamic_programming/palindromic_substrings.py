"""
Run in the neetcode text editor.
"""
class Solution:

  # Two Pointers solution (best) | Time: O(n^2), O(1)
  def countSubstrings(self, s: str) -> int:
    res = 0

    for i in range(len(s)):
      res += self.countPali(s, i, i) # odd
      res += self.countPali(s, i, i+1) # even
    return res

  def countPali(self, s, l, r):
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res += 1
      l -= 1
      r += 1
    return res