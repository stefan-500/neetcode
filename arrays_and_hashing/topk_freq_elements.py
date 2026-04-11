from collections import defaultdict
import heapq


# My solution  |  Time: O(n log n), Space: O(n)
def k_freq_elements(nums: list[int], k: int) -> list[int]:
  # result = defaultdict(int)
  # for num in nums:
  #   result[num] += 1

  # res = []
  # result = {k: v for k, v in sorted(result.items(), key= lambda item: item[1], reverse=True)}

  # j = 0
  # for key, v in result.items():
  #   if j == k:
  #     break
  #   res.append(key)
  #   j += 1

  # return f"K MOST FREQUENT ELEMENTS: {res}"

  
  # Min Heap solution  |  Time: O(n log k), Space: O(n + k)
  # count = {}
  # for num in nums:
  #     count[num] = 1 + count.get(num, 0)
  
  # heap = []
  # for num in count.keys():
  #     heapq.heappush(heap, (count[num], num))
  #     if len(heap) > k:
  #         heapq.heappop(heap)
  
  # res = []
  # for i in range(k):
  #     res.append(heapq.heappop(heap)[1])
  
  # return res


  # Bucket Sort solution (best)  |  Time: O(n), Space: O(n)
  count = {}
  freq = [[] for i in range(len(nums) + 1)]

  for num in nums:
    count[num] = 1 + count.get(num, 0)
  
  for num, cnt in count.items():
    freq[cnt].append(num)

  res = []
  for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
      res.append(num)
      if len(res) == k:
        return res




nums = [1, 1, 2, 2, 4, 3, 3, 3]
k = 2
print(k_freq_elements(nums, k))