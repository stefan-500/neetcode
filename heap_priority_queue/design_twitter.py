from typing import List
from collections import defaultdict
import heapq

"""
Run in the neetcode text editor.
"""
class Twitter:

  # Min Heap solution | Time: O(n log n) for each getNewsFeed() call and O(1) for remaining methods, Space: O(N * m + N * M + n),
  # where n is the total number of followeeIds associated with the userId,
  # m is the maximum number of tweets by any user, N is the total number of
  # userIds and M is the maximum number of followees for any user.
  def __init__(self):
    self.count = 0
    self.tweetMap = defaultdict(list)   # userId -> list of [count, tweetIds]
    self.followMap = defaultdict(set)  # userId -> set of followeeId

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.tweetMap[userId].append([self.count, tweetId])
    self.count -= 1

  def getNewsFeed(self, userId: int) -> List[int]:
    res = []
    minHeap = []

    self.followMap[userId].add(userId)
    for followeeId in self.followMap[userId]:
      if followeeId in self.tweetMap:
        index = len(self.tweetMap[followeeId]) - 1
        count, tweetId = self.tweetMap[followeeId][index]
        heapq.heappush(minHeap, [count, tweetId, followeeId,index - 1])

    while minHeap and len(res) < 10:
      count, tweetId, followeeId, index = heapq.heappop(minHeap)
      res.append(tweetId)
      if index >= 0:
        count, tweetId = self.tweetMap[followeeId][index]
        heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
    return res

  def follow(self, followerId: int, followeeId: int) -> None:
    self.followMap[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.followMap[followerId]:
      self.followMap[followerId].remove(followeeId)
