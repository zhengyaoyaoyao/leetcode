class Solution:
    def maxScore(self, s: str) -> int:
        ansMax,cur = 0,0
        number=[]
        for i in s:
            number.append(int(i))
        for i in range(1,len(number)):
            left= i-sum(number[:i])
            right = sum(number[i:])
            cur = left+right
            ansMax = max(ansMax,cur)
        return ansMax

if __name__ == '__main__':
    test = Solution()

    s="011101"
    print(test.maxScore(s))