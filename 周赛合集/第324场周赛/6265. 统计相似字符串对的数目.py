import collections
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = dict()
        for word in words:
            cur = list(set(word))
            cur = sorted(cur)
            cur = tuple(cur)
            if cur in ans.keys():
                if ans[cur]==0:
                    ans[cur]+=1
                ans[cur]+=1
            else:
                ans.setdefault(cur,0)
        sumNum = 0
        for a in ans.values():
            curNum = 0
            a-=1
            while a>0:
                curNum +=a
                a-=1
            sumNum+=curNum
        return sumNum

if __name__ == '__main__':
    test = Solution()
    words =["dcedceadceceaeddcedc","dddcebcedcdbaeaaaeab","eecbeddbddeadcbbbdbb","decbcbebbddceacdeadd","ccbddbaedcadedbcaaae","dddcaadaceaedcdceedd","bbeddbcbbccddcaceeea","bdabacbbdadabbbddaea"]
    print(test.similarPairs(words))
