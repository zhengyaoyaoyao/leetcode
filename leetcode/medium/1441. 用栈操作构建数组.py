from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        m,i,j  = len(target),1,0
        while i<=n and j<m:
            ans.append("Push")
            if target[j]!=i:
                ans.append("Pop")
            else:
                j+=1
            i+=1
        return ans