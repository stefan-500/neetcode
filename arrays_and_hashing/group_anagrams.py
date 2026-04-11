from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:

   # Best solution   Time: O(m * n), Space: O(m)
   result = defaultdict(list) # mapping charCount to list of anagrams

   for st in strs:
      # For char frequency in every word
      count = [0] * 26
      
      for char in st:
         # ord() - ASCII value of chars
         # by subtracting ord('a') the alphabetic order of the char is retrieved  
         # increment freq of that char
         count[ord(char) - ord('a')] += 1

      # Dictionary with char frequency (key), and the word (value)
      result[tuple(count)].append(st)
   
   return f"GROUP ANAGRAMS: {list(result.values())}"


   # Sorting solution   Time: O(m * nlogn) Space: O(m * n)

   # result = defaultdict(list)    # default value is []
   
   # for st in strs:
   #    # Sorted word
   #    sorted_str = "".join(sorted(st))
   #    # HashMap
   #    result[sorted_str].append(st)
      
   # return f"GROUP ANAGRAMS: {list(result.values())}

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))