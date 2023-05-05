from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        for i,value in enumerate(nums):
            if target-value in hashTable:
                return [hashTable[target-value],i]
            # 把值存进去，不是插值，是要找到每个数的插值在不在，因为是一次遍历，所以不会有自己。自己还没存进去。
            hashTable[nums[i]]=i
        return []