from typing import List

# My solution
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#   res = [0] * len(temperatures)
#   tmp = 0

#   for i in range(len(temperatures)):
#     if res[i - 1] == 0:
#       tmp = 0
#     for j in range(i + 1, len(temperatures)):
#       if temperatures[j] <= temperatures[i]:
#         tmp += 1
#       else:
#         tmp += 1
#         res[i] = tmp
#         tmp = 0
#         break

#   return res


# Brute Force solution | Time: O(n^2), Space: O(n)
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#   n = len(temperatures)
#   res = []

#   for i in range(n):
#     count = 1
#     j = i + 1
#     while j < n:
#       if temperatures[j] > temperatures[i]:
#         break
#       j += 1
#       count += 1
#     count = 0 if j == n else count
#     res.append(count)
#   return res


# Dynamic Programming solution | Time: O(n), Space: O(n)
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#   n = len(temperatures)
#   res = [0] * n

#   for i in range(n - 2, -1, -1):
#     j = i + 1
#     while j < n and temperatures[j] <= temperatures[i]:
#       if res[j] == 0:
#         j = n
#         break
#       j += res[j]
    
#     if j < n:
#       res[i] = j - i
#   return res


# Monotonic Stack solution (best) | Time: O(n), Space: O(n)
def dailyTemperatures(temperatures: List[int]) -> List[int]:
  res = [0] * len(temperatures)
  stack = []  # pair: [temp, index]

  for i, t in enumerate(temperatures):
    while stack and t > stack[-1][0]:
      stackT, stackInd = stack.pop()
      res[stackInd] = i - stackInd
    stack.append((t, i))
  return res



temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))