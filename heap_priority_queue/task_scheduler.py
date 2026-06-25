from typing import List
from collections import defaultdict, deque, Counter
import heapq

"""
Run in the neetcode text editor.
"""
class Solution:

  # My solution (explanation, and AI help)
  # def leastInterval(self, tasks: List[str], n: int) -> int:
  #   freq = defaultdict(int)
  #   for i in range(len(tasks)):
  #     freq[tasks[i]] += 1
    
  #   freqList = []
  #   for f in freq.values():
  #     freqList.append(-f)
  #   heapq.heapify(freqList)
    
  #   q = deque()
  #   time = 0
  #   while freqList or q:
  #     time += 1
  #     if freqList:
  #       task = heapq.heappop(freqList)
  #       if (task + 1) < 0: 
  #         q.append((task + 1, time + n))
  #     if q:
  #       if q[0][1] == time:
  #         heapq.heappush(freqList, q.popleft()[0])
  #   return time

  
  # Max Heap solution (best) | Time: O(m), Space: O(1) since there are at most 26 different chars;
  # where m is the number of tasks.
  def leastInterval(self, tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque() # pairs of [-cnt, idleTime]
    while maxHeap or q:
      time += 1

      if maxHeap:
        cnt = 1 + heapq.heappop(maxHeap)
        if cnt:
          q.append([cnt, time + n])
      if q and q[0][1] == time:
        heapq.heappush(maxHeap, q.popleft()[0])
    return time