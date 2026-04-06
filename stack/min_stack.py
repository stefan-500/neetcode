# My solution
# class MinStack:
#   def __init__(self):
#     self.stack = []
#     self.track = []   # to track minNum prefix

#   def push(self, val: int) -> None:
#     if not self.stack:
#       self.minNum = val 
#       self.track.append(val)
#     else:
#       self.minNum = min(self.minNum, val)
#       self.track.append(self.minNum)
    
#     self.stack.append(val)

#   def pop(self) -> None:
#     self.stack.pop()
#     self.track.pop()
#     if self.track:
#       self.minNum = self.track[-1]

#   def top(self) -> int:
#     return self.stack[-1]

#   def getMin(self) -> int:
#     return self.minNum


# Brute Force solution | Time: O(n) for getMin() and O(1) for other operations, Space: O(n) for getMin() and O(1) for other operations
# class MinStack:  
#   def __init__(self):
#     self.stack = []

#   def push(self, val: int) -> None:
#     self.stack.append(val)

#   def pop(self) -> None:
#     self.stack.pop()

#   def top(self) -> int:
#     return self.stack[-1]

#   def getMin(self) -> int:
#     tmp = []
#     mini = self.stack[-1]

#     while len(self.stack):
#       mini = min(mini, self.stack[-1])
#       tmp.append(self.stack.pop())
    
#     while len(tmp):
#       self.stack.append(tmp.pop())
    
#     return mini


# One Stack solution | Time: O(1), Space: O(n)
# class MinStack:
#   def __init__(self):
#     self.min = float('inf')
#     self.stack = []

#   def push(self, val: int) -> None:
#     if not self.stack:
#       self.stack.append(0)
#       self.min = val
#     else:
#       self.stack.append(val - self.min)
#       if val < self.min:
#         self.min = val

#   def pop(self) -> None:
#     if not self.stack:
#       return

#     pop = self.stack.pop()

#     if pop < 0:
#       self.min = self.min - pop

#   def top(self) -> int:
#     top = self.stack[-1]
#     if top > 0:
#       return top + self.min
#     else:
#       return self.min

#   def getMin(self) -> int:
#     return self.min


# Two Stacks solution (best) | Time: O(1), Space: O(n)
class MinStack:
  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]