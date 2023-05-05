from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #使用双指针，其实就是一个二次函数
        ans=[0]*len(nums)
        left,right,pos= 0,len(nums)-1,len(nums)-1
        while left<=right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                ans[pos]=nums[left]*nums[left]
                left+=1
            else:
                ans[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return ans