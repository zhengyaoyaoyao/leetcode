from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        check = 0
        ans = 0
        for x in gain:
            check+=x
            ans = max(ans,check)
        return ans