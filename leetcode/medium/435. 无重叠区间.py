from math import inf
from typing import List

#
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        dp=[0]*len(intervals)
        for x in range(len(intervals)):
            for j in range(x):
                if intervals[x][0]>=intervals[j][1]:
                    dp[x] = max(dp[x],dp[j]+1)
        return len(intervals)-dp[-1]-1

'''
贪心的思想解题：
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals is None:
            return 0
        cur,res = -inf,0
        intervals.sort(key=lambda p:p[1])
        for x,y in intervals:
            if cur <=x:
                cur = y
                res +=1
        return len(intervals)-res

if __name__ == '__main__':
    intervals = [[1,2],[1,2],[1,2]]
    test = Solution()
    print(test.eraseOverlapIntervals(intervals))

