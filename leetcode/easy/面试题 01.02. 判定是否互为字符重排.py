import collections


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        count2 = collections.Counter(s2)
        count1 = collections.Counter(s1)
        return count1==count2


if __name__ == '__main__':
    s1 = "abc"
    s2 = "bca"
    test = Solution()
    print(test.CheckPermutation(s1,s2))