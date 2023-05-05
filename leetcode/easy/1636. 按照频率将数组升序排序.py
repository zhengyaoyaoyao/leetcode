import collections
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        record = collections.Counter(nums)
        nums.sort(key = lambda x:record[x])
        return nums
if __name__ == '__main__':
    test = Solution()
    nums = [-1,1,-6,4,5,-6,1,4,1]
    print(test.frequencySort(nums))