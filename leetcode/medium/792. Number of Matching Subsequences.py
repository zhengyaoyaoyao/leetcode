import collections
from bisect import bisect_right
from typing import List



'''
暴力超时
'''
class Solution1:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isCheck(s,t):
            index1= 0
            index2=0
            while index1<len(s) and index2 <len(t):
                if s[index1] == t[index2]:
                    index1+=1
                index2+=1
            if index1==len(s):
                return True
            if index2==len(t):
                return False
        ans = 0
        for x in words:
            ans += 1 if isCheck(x,s) else 0
        return ans
'''
算法优化
使用二分查找
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = collections.defaultdict(list)
        for i,c in enumerate(s):
            pos[c].append(i)
        ans = len(words)
        for w in words:
            if len(w)>len(s):
                ans -=1
                continue
            p = -1
            for c in w:
                ps=pos[c]
                j = bisect_right(ps,p)
                if j==len(ps):
                    ans -=1
                    break
                p = ps[j]
        return ans


if __name__ == '__main__':
    s = "dsahjpjauf"
    words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
    test = Solution()
    print(test.numMatchingSubseq(s,words))