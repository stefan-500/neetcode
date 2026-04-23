# My solution (wathed explanation and some code)
# def characterReplacement(s: str, k: int) -> int:
#   count = {}
#   l = 0
#   res = 0
#   maxFreq = 0
  
#   for r in range(len(s)):
#     count[s[r]] = 1 + count.get(s[r], 0)
#     maxFreq = max(maxFreq, count[s[r]])
    
#     if ((r - l + 1) - maxFreq) <= k:
#       res = max(res, r - l + 1)
#     else:
#       count[s[l]] -= 1
#       l += 1
#   return res


# Brute Force solution | Time: O(n^2), Space: O(m), where
# n is the length of the string and m is the total number of unique characters in the string.
# def characterReplacement(s: str, k: int) -> int:
#   res = 0
#   for i in range(len(s)):
#     count = {}
#     maxf = 0
#     for j in range(i, len(s)):
#       count[s[j]] = 1 + count.get(s[j], 0)
#       maxf = max(maxf, count[s[j]])
#       if (j - i + 1) - maxf <= k:
#         res = max(res, j - i + 1)
#   return res


# Sliding Window solution (best) | Time: O(n), Space: O(m), where
# n is the length of the string and m is the total number of unique characters in the string.
def characterReplacement(s: str, k: int) -> int:
  count = {}
  res = 0

  l = 0
  maxf = 0
  for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    maxf = max(maxf, count[s[r]])
    
    while (r - l + 1) - maxf > k:
      count[s[l]] -= 1
      l += 1
    res = max(res, r - l + 1)

  return res



s = "XYYX"
k = 2
print(characterReplacement(s, k))