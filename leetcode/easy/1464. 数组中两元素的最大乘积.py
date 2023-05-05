from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    cur=(nums[i]-1)*(nums[j]-1)
                    maxValue = max(cur,maxValue)
        return maxValue

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)