from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]>=len(nums):
            return len(nums)
        for i in range(1,len(nums)):
            x = len(nums)-i
            if nums[i]>=x>nums[i-1]:
                return x
        return -1