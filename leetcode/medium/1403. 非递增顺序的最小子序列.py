from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if sum(nums[i:])>sum(nums[0:i]):
                ans = nums[i:]
                ans.sort(reverse=True)
                return ans

