from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left+=1
        return left

# 把双指针放到头尾
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)
        while left<right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right-=1
            else:
                left+=1
        return left