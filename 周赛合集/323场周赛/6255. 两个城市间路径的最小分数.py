import collections
import math
from typing import List


class Solution:
    class Solution:
        def minScore(self, n: int, roads: List[List[int]]) -> int:
            g = [[] for _ in range(n)]
            for x, y, d in roads:
                g[x - 1].append((y - 1, d))
                g[y - 1].append((x - 1, d))
            ans = math.inf
            vis = [False] * n

            def dfs(x: int) -> None:
                nonlocal ans
                vis[x] = True
                for y, d in g[x]:
                    ans = min(ans, d)
                    if not vis[y]:
                        dfs(y)
            dfs(0)
            return ans
if __name__ == '__main__':
    n = 4
    roads = [[1,2,2],[1,3,4],[3,4,7]]
    test=Solution()
    print(test.minScore(n, roads))