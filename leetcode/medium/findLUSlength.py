from typing import List


class Solution:
    def findLUSlength(self,strs:List[str]) ->int:
        def is_subseg(s:str,t:str) -> bool:
            pt_s = pt_t = 0
            while  pt_s<len(s) and pt_t <len(t):
                if s[pt_s] ==t[pt_t]:
                    pt_s+=1
                pt_t+=1
            return pt_s == len(s)
        ans =-1
        for i,s in enumerate(strs):
            check = True
            for j,t in enumerate(strs):
                if i!=j and is_subseg(s,t):
                    check =False
                    break
            if check:
                ans = max(ans,len(s))
        return ans