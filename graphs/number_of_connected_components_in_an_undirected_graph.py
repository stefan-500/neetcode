from typing import List

"""
Run in the neetcode text editor.
"""
class Solution:

  # DFS solution (best) | Time: O(V + E), Space: O(V + E),
  # where V is the number of vertices and E is the number of edges in the graph.
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    adj = [[] for _ in range(n)]
    visit = [False] * n
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    def dfs(node):
      for nei in adj[node]:
        if not visit[nei]:
          visit[nei] = True
          dfs(nei)

    res = 0
    for node in range(n):
      if not visit[node]:
        visit[node] = True
        dfs(node)
        res += 1
    return res