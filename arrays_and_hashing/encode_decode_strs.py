from typing import List

# My solution

# DELIM = "😂"
# def encode(strs: List[str]) -> str:
#   encoded = ""
#   for s in strs:
#     encoded += s + DELIM
  
#   return(encoded)


# def decode(s: str) -> List[str]:
#   decoded = []
  
#   while len(s) > 0:
#     prev = s[:s.find(DELIM)]
#     s = s[s.find(DELIM)+1:]
#     decoded.append(prev)

#   return decoded

# Neetcode solution 1  |  Time: O(m), Space: O(m + n)

# def encode(strs: List[str]) -> str:
#   if not strs:
#     return ""
  
#   sizes = []
#   res = ""
  
#   for s in strs:
#     sizes.append(len(s))
#   for sz in sizes:
#     res += str(sz)
#     res += ","
#   res += "#"

#   for s in strs:
#     res += s
  
#   return res

# def decode(s: str) -> List[str]:
#   if not s:
#     return []
  
#   sizes, res = [], []
#   i = 0
#   while s[i] != '#':
#     cur = ""
#     while s[i] != ',':
#       cur += s[i]
#       i += 1
#     sizes.append(int(cur))
#     i += 1
#   i += 1

#   for sz in sizes:
#     res.append(s[i:i + sz])
#     i += sz
  
#   return res

# Best solution  |  Time: O(m), Space: O(m + n)
def encode(strs: List[str]) -> str:
  res = ""
  
  for s in strs:
    res += str(len(s)) + "#" + s
  
  return res

def decode(s: str) -> List[str]:
  res = []
  i = 0

  while i < len(s):
    j = i
    while s[j] != "#":
      j += 1
  
    length = int(s[i:j])
    i = j + 1
    j = i + length
    res.append(s[i:j])
    i = j
  
  return res

test = ["Hello", "World", "Hi a", "Hi b"]
print(decode(encode(test)))