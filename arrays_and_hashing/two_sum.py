def twoSum(nums: list[int], target: int) -> list[int]:
  # My solution
  # for i in range(len(nums)):
  #   for j in range(i+1, len(nums)):
  #     if nums[i] + nums[j] == target:
  #       indices = [i, j]
  #       return indices


  # Sorting solution  Time: O(n log n), Space: 0(n) 
  # A = []
  # for i, num in enumerate(nums):
  #   A.append([num, i])
  
  # A.sort()
  # i, j = 0, len(nums) - 1
  # while i < j:
  #   cur = A[i][0] + A[j][0]
  #   if cur == target:
  #     return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
  #   elif cur < target:
  #     i += 1 
  #   else:
  #     j -= 1
  # return []


  # Hash Map solution 1  Time: O(n), Space: 0(n)
  # indices = {}  # value -> index

  # for i, n in enumerate(nums):
  #   indices[n] = i

  # for i, n in enumerate(nums):
  #   diff = target - n
  #   if diff in indices and indices[diff] != i:
  #     return [i, indices[diff]]


  # Hash Map solution 2  Time: O(n), Space: 0(n) 
  prevMap = {}  # value -> index
  for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i

  
    
nums = [4, 5, 6]
target = 10
print(twoSum(nums, target))