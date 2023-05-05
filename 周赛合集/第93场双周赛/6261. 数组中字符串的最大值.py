from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for x in strs:
            if x.isdigit():
                cur = int(x)
            else:
                cur =len(x)
            ans = max(cur,ans)
        return ans