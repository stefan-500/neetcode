from typing import List
import operator

# My 1. solution
# def evalRPN(tokens: List[str]) -> int:
#   operators = set(('+', '-', '*', '/'))
#   # operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
#   stack = []
  
#   for t in tokens:
#     if t not in operators:
#       stack.append(t)
#     else:
#       opnd2 = int(stack.pop())
#       opnd1 = int(stack.pop())
#       if t == '+':
#         res = opnd1 + opnd2
#       elif t == '-':
#         res = opnd1 - opnd2
#       elif t == '*':
#         res = opnd1 * opnd2
#       else:
#         res = opnd1 / opnd2
#       stack.append(res)

#   return int(stack.pop())


# Brute Force solution | Time: O(n^2), Space: O(n)
# def evalRPN(self, tokens: List[str]) -> int:
#   while len(tokens) > 1:
#     for i in range(len(tokens)):
#       if tokens[i] in "+-*/":
#         a = int(tokens[i-2])
#         b = int(tokens[i-1])
#         if tokens[i] == '+':
#           result = a + b
#         elif tokens[i] == '-':
#           result = a - b
#         elif tokens[i] == '*':
#           result = a * b
#         elif tokens[i] == '/':
#           result = int(a / b)
#         tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
#         break
#   return int(tokens[0])


# Brute Force solution
# def evalRPN(tokens: List[str]) -> int:
#   operators = { "+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv }
#   stack = []
  
#   for t in tokens:
#     if t not in operators:
#       stack.append(t)
#     else:
#       opnd2 = int(stack.pop())
#       opnd1 = int(stack.pop())
#       # Apply the operation matching the current operator to the operands
#       res = operators[t](opnd1, opnd2)    # same as e.g. operator.add(2, 3)
#       stack.append(res)

#   return int(stack.pop())


# Doubly Linked List solution | Time: O(n), Space: O(n)
# class DoublyLinkedList:
#   def __init__(self, val, next=None, prev= None):
#     self.val = val
#     self.next = next
#     self.prev = prev

# class Solution:
#   def evalRPN(self, tokens: List[str]) -> int:
#     head = DoublyLinkedList(tokens[0])
#     curr = head

#     for i in range(1, len(tokens)):
#       curr.next = DoublyLinkedList(tokens[i], prev=curr)
#       curr = curr.next

#     while head is not None:
#       if head.val in "+-*/":
#         l = int(head.prev.prev.val)
#         r = int(head.prev.val)
#         if head.val == '+':
#           res = l + r
#         elif head.val == '-':
#           res = l - r
#         elif head.val == '*':
#           res = l * r
#         else:
#           res = int(l / r)
        
#         head.val = str(res)
#         head.prev = head.prev.prev.prev
#         if head.prev is not None:
#           head.prev.next = head

#       ans = int(head.val)
#       head = head.next

#     return ans


# My 2. Stack solution (better)
def evalRPN(tokens: List[str]) -> int:
  # operators = { "+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv }
  # Variation without operator module (from youtube)
  operators = { "+" : lambda l, r: l + r, "-" : lambda l, r: l - r, "*" : lambda l, r: l * r, "/" : lambda l, r: l / r }
  stack = []
  
  for t in tokens:
    if t not in operators:
      stack.append(t)
    else:
      opnd2 = int(stack.pop())
      opnd1 = int(stack.pop())
      # Apply the operation matching the current operator to the operands
      res = operators[t](opnd1, opnd2)    # same as e.g. operator.add(2, 3)
      stack.append(res)

  return int(stack.pop())



tokens = ["1","2","+","3","*","4","-"]
# tokens = ["2", "1", "-", "3", "/"]
print(evalRPN(tokens))