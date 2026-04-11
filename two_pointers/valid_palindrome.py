import re


# My solution
# def isPalindrome(s: str) -> bool:
#   sAlpha = re.sub(r'\W+', '', s).lower()
#   sAlphaBackwards = ""
#   for c in range(len(sAlpha) - 1, -1, -1):
#     sAlphaBackwards += sAlpha[c]

#   if sAlpha == sAlphaBackwards:
#     return True
  
#   return False


# My 2. solution
# def isPalindrome(s: str) -> bool:
#   sAlpha = re.sub(r'\W+', '', s).lower()
#   br = 0
#   res = True
  
#   for c in range(len(sAlpha) - 1, -1, -1):
#     # print(f"c:{c} {sAlpha[c]}, br:{br} {sAlpha[br]}")
#     if sAlpha[c] != sAlpha[br]:
#       res = False
#       return res
    
#     if br > c:
#       return res
    
#     br += 1
#   return res


# Reverse string solution | Time: O(n), Space: O(n)
def isPalindrome(s: str) -> bool:
  newStr = ''
  for c in s:
    if c.isalnum():
      newStr += c.lower()
  return newStr == newStr[::-1]   # [::-1} means 'make a reversed copy'


# Two Pointers solution | Time: O(n), Space: O(1)  
# def isPalindrome(s: str) -> bool:
#   l = 0
#   r = len(s) - 1
  
#   while l < r:
#     while l < r and not alphaNum(s[l]):
#       l += 1
#     while r > l and not alphaNum(s[r]):
#       r -= 1

#     if s[l].lower() != s[r].lower():
#       return False
#     l += 1
#     r -= 1
#   return True

# def alphaNum(c):
#   return (ord('A') <= ord(c) <= ord('Z') or
#           ord('a') <= ord(c) <= ord('z') or
#           ord('0') <= ord(c) <= ord('9'))



s = "Was it a car or a cat I saw?"
print(isPalindrome(s))