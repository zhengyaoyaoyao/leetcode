import collections
'''
遇到轮转的问题，因为是一个循环，所以如果把要匹配的字符串复制一下，即s1+s1，那么就会出现整个轮转的字符串
'''

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2)  and s2 in s1+s1
if __name__ == '__main__':
    s1 = "aa"
    s2 = "aba"
    test = Solution()
    print(test.isFlipedString(s1,s2))