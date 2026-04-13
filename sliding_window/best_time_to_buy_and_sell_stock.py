from typing import List


# My solution
# def maxProfit(prices: List[int]) -> int:
#   currMax = 0
#   for i in range(len(prices)):
#     for j in range(i + 1, len(prices)):
#       if prices[j] > prices[i]:
#         currMax = max(currMax, prices[j] - prices[i])
#   return currMax


# Brute Force solution | Time: O(n^2), Space: O(1)
# def maxProfit(prices: List[int]) -> int:
#   res = 0
#   for i in range(len(prices)):
#     buy = prices[i]
#     for j in range(i + 1, len(prices)):
#       sell = prices[j]
#       res = max(res, sell - buy)
#   return res


# Dynamic Programming solution | Time: O(n), Space: O(1)
# def maxProfit(prices: List[int]) -> int:
#   maxP = 0
#   minBuy = prices[0]

#   for sell in prices:
#     maxP = max(maxP, sell - minBuy)
#     minBuy = min(minBuy, sell)
#   return maxP


# Two Pointers solution (best) | Time: O(n), Space: O(1)
def maxProfit(prices: List[int]) -> int:
  l = 0
  r = 1
  maxP = 0

  while r < len(prices):
    if prices[l] < prices[r]:
      profit = prices[r] - prices[l]
      maxP = max(maxP, profit)
    else:
      l = r
    r += 1
  return maxP



prices=[5,1,5,6,7,1,10]
print(maxProfit(prices))