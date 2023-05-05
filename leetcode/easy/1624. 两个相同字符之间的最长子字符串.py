class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        maxValue = -1
        for i in range(n):
            for j in range(n-1,i,-1):
                if s[i]==s[j]:
                    maxValue = max(j-i-1,maxValue)
        return maxValue

'''
用字典去存下标的位置，然后之后如果再遇到，那么就减去下标就好了。
'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        firstIndex={}
        for index,value  in enumerate(s):
            if value not in firstIndex:
                firstIndex[value]=index
            else:
                ans  = max(ans,index-firstIndex[value]-1)
        return ans


if __name__ == '__main__':
    s="mgntdygtxrvxjnwksqhxuxtrv"
    test = Solution()
    print(test.maxLengthBetweenEqualCharacters(s))