from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre= 0
        maxAns = nums[0]
        for i in nums:
            pre = max(pre+i,i)
            maxAns = max(maxAns,pre)
        return maxAns

