from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        minv = [0] * (n + 10)
        minv[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            minv[i] = min(minv[i + 1], nums[i])
        maxv = 0
        for i in range(n - 1):
            maxv = max(maxv, nums[i])
            if maxv <= minv[i + 1]:
                return i + 1
        return -1
