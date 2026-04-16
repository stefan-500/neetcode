

# Brute Force solution | Time: O(n * m), Space: O(m),
# where n is the length of the string and m is the total number of unique characters in string
# def lengthOfLongestSubstring(s: str) -> int:
#   res = 0
#   for i in range(len(s)):
#     charSet = set()
#     for j in range(i, len(s)):
#       if s[j] in charSet:
#         break
#       charSet.add(s[j])
#     res = max(res, len(charSet))
#   return res


# Sliding Window solution (best) | Time: O(n), Space: O(m),
# where n is the length of the string and m is the total number of unique characters in string
def lengthOfLongestSubstring(s: str) -> int:
  res = 0
  charset = set()
  l = 0
  
  for r in range(len(s)):
    while s[r] in charset:
      charset.remove(s[l])
      l += 1
    charset.add(s[r])
    res = max(res, r - l + 1)
  return res


# Sliding Window 2. solution (but less readable) | Time: O(n), Space: O(m),
# where n is the length of the string and m is the total number of unique characters in string
# def lengthOfLongestSubstring(s: str) -> int:
#   mp = {}
#   l = 0
#   res = 0

#   for r in range(len(s)):
#     if s[r] in mp:
#       l = max(mp[s[r]] + 1, l)
#     mp[s[r]] = r
#     res= max(res, r - l + 1)
#   return res



s = "dvdf"
print(lengthOfLongestSubstring(s))