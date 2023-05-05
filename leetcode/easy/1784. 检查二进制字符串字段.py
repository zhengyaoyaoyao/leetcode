class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        index = 0
        for i in range(len(s)):
            if s[i] =='1':
                index=i
        for i in range(index):
            if s[i]!='1':
                return False
        else:
            return True

if __name__ == '__main__':
    s= "110"
    test = Solution()
    print(test.checkOnesSegment(s))
