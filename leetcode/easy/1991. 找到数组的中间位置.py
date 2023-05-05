from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ans =-1
        for i in range(len(nums)):
            if i ==0:
                if sum(nums[i+1:])==0:
                    return 0
            if i ==len(nums)-1:
                if sum(nums[:i])==0:
                    return i
            if sum(nums[:i]) == sum(nums[i+1:]):
                ans= i
                break
        return ans

'''
前缀和思想可解
左侧求和为:sum
此时右侧为：total-sum-num[i]
相等则:sum = total- sum-num[i]
即满足条件时：2*sum+num[i] = total
'''
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if (2*leftSum+nums[i]==total):
                return i
            leftSum+=nums[i]
        return -1;

