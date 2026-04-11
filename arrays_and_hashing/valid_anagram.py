# My solution      
def isAnagram(s: str, t: str) -> bool:
  # if len(t) != len(s):
  #   return False

  # chars = []
  # for i in s:
  #   chars.append(i)
  # for c in t:
  #   if c not in chars:
  #     return False
  #   chars.remove(c)
  # return True

  # Sorting solution   Time: O(n log n + m log m),  Space: O(1) ili O(n + m) depending on sorting algorithm
  # if len(s) != len(t):
  #   return False
            
  # return sorted(s) == sorted(t)


  # Hash Map solution 1  Time: O(n + m), Space: O(1)
  if len(s) != len(t):
    return False

  countS, countT = {}, {}

  for i in range(len(s)):
      countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)
  
  return countS == countT 


  # Hash Map solution 2   Time: O(n + m), Space: 0(1) 
  # if len(s) != len(t):
  #   return False

  # count = [0] * 26
  # for i in range(len(s)):
  #     count[ord(s[i]) - ord('a')] += 1
  #     count[ord(t[i]) - ord('a')] -= 1

  # for val in count:
  #     if val != 0:
  #         return False
  # return True


s = 'racecar'
t = 'carrace'
print(isAnagram(s, t))
