from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        checkNum = [0]*len(nums)*2
        for i in range(len(nums)):
            j = i+len(nums)
            checkNum[i] = nums[i]
            checkNum[j] = nums[i]
        count = 1
        for i in range(1,len(checkNum)):
            if count == len(nums):
                return True
            if checkNum[i]-checkNum[i-1]>=0:
                count+=1
            else:
                count=1
        return False

if __name__ == '__main__':
    nums = [6]
    test=Solution()
    test.check(nums)
