from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        idx = 0
        for x in nums:
            if idx < k or nums[idx - k] != x:
                nums[idx] = x
                idx += 1
        return idx


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    test = Solution()
    print(test.removeDuplicates(nums))
