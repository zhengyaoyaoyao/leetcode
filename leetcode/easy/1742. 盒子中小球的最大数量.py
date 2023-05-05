import collections


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans = collections.Counter()
        while lowLimit<=highLimit:
            check = lowLimit
            NumSum = 0
            while check!=0:
                a = check%10
                check =check//10
                NumSum+=a
            ans[NumSum]+=1
            lowLimit+=1
        return max(ans.values())

if __name__ == '__main__':
    lowLimit = 1
    highLimit = 10
    test = Solution()
    print(test.countBalls(lowLimit,highLimit))
