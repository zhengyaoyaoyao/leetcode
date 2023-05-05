import collections
from typing import List


class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slow = 0
        fast = slow+len(p)
        ans =list()
        pCount = collections.Counter(p)
        while fast<=len(s):
            check = s[slow:fast]
            if collections.Counter(check) == pCount:
                ans.append(slow)
            slow+=1
            fast+=1
        return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = list()
        n,m=  len(s),len(p)
        cnt = [0]*26
        for i in range(m):
            cnt[ord(p[i])-ord('a')]+=1
        #统计有多少个词
        a=0
        for i in range(26):
            if cnt[i] !=0:
                a+=1
        l,r,b = 0,0,0
        while r<n:
            cnt[ord(s[r]) - ord('a')]-= 1
            if cnt[ord(s[r]) - ord("a")]==0:
                b+=1
            if r-l+1>m:
                cnt[ord(s[l])-ord("a")]+=1
                if cnt[ord(s[l])-ord("a")]==1:
                    b-=1
                l+=1
            if b==a:
                ans.append(l)
            r+=1
        return ans


if __name__ == '__main__':
    s = "aa"
    p = "bb"
    test =Solution()
    print(test.findAnagrams(s, p))