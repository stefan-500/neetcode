# My solution (watched explanation and code part)
# def isValid(s: str) -> bool:
#   mp = {')': '(', ']': '[', '}': '{'}   # kljucno
#   opening = set(('(', '{', '['))
#   stack = []
  
#   for i in range(len(s)):
#     if s[i] in opening:
#       stack.append(s[i])
#       continue
#     else:
#       if not stack:
#         return False
#       if mp[s[i]] and mp[s[i]] == stack[-1]:
#         stack.pop()
#         continue
#       else:
#         return False
#   if not stack:
#     return True
#   return False


# Brute Force solution | Time: O(n^2), Space: O(n)
# def isValid(s: str) -> bool:
#   while '()' in s or '{}' in s or '[]' in s:
#     s = s.replace('()', '')
#     s = s.replace('{}', '')
#     s = s.replace('[]', '')
#   return s ==''


# Stack solution (best) | Time: O(n), Space: O(n)
def isValid(s: str) -> bool:
  stack = []
  closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

  for c in s:
    if c in closeToOpen:    # checks dict keys
      if stack and stack[-1] == closeToOpen[c]:   # checks fict value at a key
        stack.pop()
      else:
        return False
    else:
      stack.append(c)

  return True if not stack else False



s = "([{}])"
print(isValid(s)) 