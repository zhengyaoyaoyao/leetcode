import math
from typing import List


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if edges is None:
            return vals[0]
        n = len(vals)
        g = [[-10e-4]*n for _ in range(n)]
        for x, y in edges:
            g[x][y] = vals[y]
            g[y][x] = vals[x]
        ans = float("-inf")
        for index,value in enumerate(g):
            cur = vals[index]
            count =0
            value.sort(reverse=True)
            for i in range(n):
                if(value[i])>0 and count<k:
                    count+=1
                    cur+=value[i]
            ans = max(cur,ans)
        return ans
class Solution1:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if edges is None:
            return vals[0]
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append((y,vals[y]))
            g[y].append((x,vals[x]))
        for i in g:
            i.sort(key=lambda x:x[1],reverse=True)
        ans = float("-inf")
        for j,i in enumerate(g):
            count = 0
            cur = vals[j]
            for index,(value1,value2) in enumerate(i):
                if value2>0 and count<k:
                    cur +=value2
                    count+=1
            ans = max(cur,ans)
        return ans

if __name__ == '__main__':
    test = Solution1()
    vals = [0,-36,4,35,27,-13]
    edges =  [[5,3],[4,3],[0,4],[2,4],[0,2]]
    k = 1
    print(test.maxStarSum(vals, edges, k))






