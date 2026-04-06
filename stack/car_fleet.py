from typing import List


# Stack solution (best) | Time: O(n log n), Space: O(n)
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
  pair = [[p, s] for p, s in zip(position, speed)]
  pair.sort(reverse=True)
  
  stack = []
  for p, s in pair:   # reverse sorted order
    stack.append((target - p) / s)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  return len(stack)


# Iteration solution | Time: O(n log n), Space: O(n)
# def carFleet(target: int, position: List[int], speed: List[int]) -> int:
#   pair = [(p, s) for p, s in zip(position, speed)]
#   pair.sort(reverse=True)

#   fleets = 1
#   prevTime = (target - pair[0][0]) / pair[0][1]
#   for i in range(1, len(pair)):
#     currCar = pair[i]
#     currTime = (target - currCar[0]) / currCar[1]
#     if currTime > prevTime:
#       fleets += 1
#       prevTime = currTime
#   return fleets


print(carFleet(target=10, position=[1, 4], speed=[3, 2]))
