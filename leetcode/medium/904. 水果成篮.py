import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = collections.Counter()
        left = ans = 0
        for right,x in enumerate(fruits):
            cnt[x]+=1 # 把右边这个数进入哈希表
            while len(cnt)>2:
                cnt[fruits[left]]-=1
                if cnt[fruits[left]]==0:
                    cnt.pop(fruits[left])
                left+=1
            ans = max(ans,right-left+1)
        return ans


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = collections.Counter()
        start = ans = 0
        for end,value in enumerate(fruits):
            cnt[value]+=1 #每次都往前移动。
            while len(cnt)>2:
                cnt[fruits[start]]-=1
                if cnt[fruits[start]] ==0:
                    cnt.pop(fruits[start])
                start+=1
            ans = max(ans,end-start+1)
        return ans


