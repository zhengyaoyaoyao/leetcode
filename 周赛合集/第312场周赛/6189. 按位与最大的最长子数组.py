from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxValue = max(nums)
        ans = 0
        maxlength =0
        for index,value in enumerate(nums):
            if value == maxValue:
                ans+=1
                maxlength = max(ans,maxlength)
            else:
                ans=0
        return maxlength
