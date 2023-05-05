from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        maxValue = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]
            maxValue = max(cur, maxValue)
        return maxValue


if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50]
    test = Solution()
    print(test.maxAscendingSum(nums))
