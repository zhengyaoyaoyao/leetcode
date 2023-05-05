from math import inf
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        maxlength = 1
        pairs.sort(reverse=True)
        for x in range(len(pairs)-1):
            curLength=1
            #从x开始，那么目前值就是x的值，最后一个不需要
            cur=pairs[x][0]
            for i in range(x+1,len(pairs)):
                if cur>pairs[i][1]:
                    cur=pairs[i][0]
                    curLength+=1
            maxlength = max(maxlength,curLength)
        return maxlength
#动态规划
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        #先对其排序，然后创建一个数组，不断的在前面找即可。
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]

'''贪心的解题：
要挑选最长数对链的第一个数对时，最优的选择是挑选第二个数字最小的，这样能给挑选后续的数对留下更多的空间。
挑完第一个数对后，要挑第二个数对时，也是按照相同的思路，是在剩下的数对中，第一个数字满足题意的条件下，挑选第二个数字最小的。
按照这样的思路，可以先将输入按照第二个数字排序，然后不停地判断第一个数字是否能满足大于前一个数对的第二个数字即可。
'''
class Solution(object):
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res

if __name__ == '__main__':
    pairs = [[2,2], [1,3], [3,4]]
    pairs.sort(reverse=True)
    print(pairs)
