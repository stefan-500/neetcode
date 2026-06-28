import heapq

"""
Run in the neetcode text editor.
"""
class MedianFinder:

  # My solution (with explanation)
  # def __init__(self):
  #   self.nums = []

  # def addNum(self, num: int) -> None:
  #   self.nums.append(num)
  #   self.nums = sorted(self.nums)

  # def findMedian(self) -> float:
  #   if len(self.nums) % 2 == 0:
  #     a = (len(self.nums) // 2) - 1
  #     b = a + 1
  #     return (self.nums[a] + self.nums[b]) / 2
  #   else:
  #     return self.nums[len(self.nums) // 2]


  # Heap solution (best) | Time: O(m * log n) for addNum(), O(m) for findMedian(), Space: O(n);
  # where m is the number of function calls and n is the length of the array.
  def __init__(self):
    # two heaps, large, small, minheap, maxheap
    # heaps should be approx. equal size
    self.small, self.large = [], []

  def addNum(self, num: int) -> None:
    if self.large and num > self.large[0]:
      heapq.heappush(self.large, num)
    else:
      heapq.heappush(self.small, -1 * num)

    if len(self.small) > len(self.large) + 1:
      val = -1 * heapq.heappop(self.small)
      heapq.heappush(self.large, val)
    elif len(self.large) > len(self.small) + 1:
      val = heapq.heappop(self.large)
      heapq.heappush(self.small, -1 * val)

  def findMedian(self) -> float:
    if len(self.small) > len(self.large):
      return -1 * self.small[0]
    elif len(self.large) > len(self.small):
      return self.large[0]

    return (-1 * self.small[0] + self.large[0]) / 2