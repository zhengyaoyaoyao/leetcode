from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        left = 0
        right = len(nums)-1
        while left<len(nums):
            if nums[left] == target:
                break
            left+=1
        while right>0:
            if nums[right]==target:
                break
            right-=1
        return [left,right]


# 用二分的办法做，left和right分开坐

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums,target,lower):
            left = 0
            right= len(nums)-1
            ans = len(nums)
            while left<=right:
                mid = left+right>>1
                if (nums[mid] >target) or (lower and nums[mid] >=target):
                    right= mid-1
                    ans = mid
                else:
                    left =mid+1
            return ans
        leftIdx = binarySearch(nums,target,True)
        rightIdx = binarySearch(nums,target,False)-1
        if leftIdx<=rightIdx and rightIdx<len(nums) and nums[leftIdx]==target and nums[rightIdx]==target:
            return [leftIdx,rightIdx]
        return [-1,-1]
