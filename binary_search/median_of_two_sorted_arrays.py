from typing import List


# My solution (not efficient) (AI helped)
# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
#   nums = sorted(nums1 + nums2)
#   n = len(nums)
  
#   if n % 2 == 0:  # even array length
#     median = (nums[(n // 2) - 1] + nums[n // 2]) / 2
#   else:
#     median = float(nums[n // 2])
#   return median


# Brute Force solution | Time: O((n + m) log (n + m)), Space: O(n + m), 
# where n is the length of nums1 and m is the length of nums2
# def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
#   len1 = len(nums1)
#   len2 = len(nums2)
#   merged = nums1 + nums2
#   merged.sort()

#   totalLen = len(merged)
#   if totalLen % 2 == 0:
#     return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
#   else:
#     return merged[totalLen // 2]


# Binary Search solution (best) | Time: O(log(min(n, m))), Space: O(1), 
# where n is the length of nums1 and m is the length of nums2
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
  A = nums1
  B = nums2
  total = len(nums1) + len(nums2)
  half = total // 2 # round down if even (half can be approximate)

  if len(B) < len(A):
    A, B = B, A  # swap

  l = 0
  r = len(A) - 1
  while True:
    i = (l + r) // 2
    j = half - i - 2

    Aleft = A[i] if i >= 0 else float("-infinity")
    Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
    Bleft = B[j] if j >= 0 else float("-infinity")
    Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

    if Aleft <= Bright and Bleft <= Aright: # valid subpart
      if total % 2: # odd
        return min(Aright, Bright)
      return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
    elif Aleft > Bright:
      r = i - 1
    else:
      l = i + 1



# nums1 = [1, 2]
# nums2 = [3]

nums1 = [1,3]
nums2 = [2,4]
print(findMedianSortedArrays(nums1, nums2))