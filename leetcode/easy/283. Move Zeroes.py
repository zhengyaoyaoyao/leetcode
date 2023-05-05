from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast< len(nums):
            if nums[fast] !=0:
                nums[fast],nums[slow]=nums[slow],nums[fast]
                slow+=1
            fast+=1
if __name__ == '__main__':
    nums =[1]
    test = Solution()
    print(test.moveZeroes(nums))