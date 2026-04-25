# Brute Force solution | Time: O(n^2 * m), Space: O(m), where
# n is the length of the string s and m is the total number of unique chars
# in the strings t and s.
# def minWindow(s: str, t: str) -> str:
#   if t == "":
#     return ""

#   countT = {}
#   for c in t:
#     countT[c] = 1 + countT.get(c, 0)

#   res = [-1, -1]
#   resLen = float("infinity")
#   for i in range(len(s)):
#     countS = {}
#     for j in range(i, len(s)):
#       countS[s[j]] = 1 + countS.get(s[j], 0)

#       flag = True
#       for c in countT:
#         if countT[c] > countS.get(c, 0):
#           flag = False
#           break
      
#       if flag and (j - i + 1) < resLen:
#         resLen = j - i + 1
#         res = [i, j]

#   l, r = res
#   return s[l : r + 1] if resLen != float("infinity") else ""


# Sliding Window solution (best) | Time: O(n + m), Space: O(m), where
# n is the length of the string s and m is the total number of unique chars
# in the strings t and s.
def minWindow(s: str, t: str) -> str:
  if t == "":
    return ""

  countT = {}
  window = {}
  for c in t:
    countT[c] = 1 + countT.get(c, 0)

  have = 0
  need = len(countT)
  res = [-1, -1]
  resLen = float("infinity")
  l = 0
  for r in range(len(s)):
    c = s[r]
    window[c] = 1 + window.get(c, 0)

    if c in countT and window[c] == countT[c]:
      have += 1
    
    while have == need:
      if (r - l + 1) < resLen:
        res = [l, r]
        resLen = r - l + 1

      window[s[l]] -= 1
      if s[l] in countT and window[s[l]] < countT[s[l]]:
        have -= 1
      l += 1
  l, r = res
  return s[l : r + 1] if resLen != float("infinity") else ""



s = "OUZODYXAZV"
t = "XYZ"
print(minWindow(s, t))