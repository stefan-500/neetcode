nums = [1, 2, 3, 3]

# Brute force solution     Time: O(n^2),  Space: O(1)
# for i in range(len(nums)):
#   for j in range(i+1, len(nums)):
#     if nums[i] == nums[j]:
#       has_duplicate = True
#     else:
#       has_duplicate = False
# print(has_duplicate)

# Sorting solution         Time: O(n log n),  Space: O(1) ili O(n) depending on the sorting algorithm
# When the array is sorted duplicates will be adjecent,
# so only one iteration is needed.
# nums.sort()
# for i in range(1, len(nums)):
#   if nums[i] == nums[i - 1]:
#     has_duplicate = True
#   else:
#     has_duplicate = False
# print(has_duplicate)

# Hash Set solution        Time: O(n),  Space: O(n)
seen_elements = set()
for num in nums:
  if num in seen_elements:
    has_duplicate = True
  else:
    seen_elements.add(num)
    has_duplicate = False



print(has_duplicate)