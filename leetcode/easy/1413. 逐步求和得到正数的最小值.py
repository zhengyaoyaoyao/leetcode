from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        numSum=0
        minNum=1
        for value in nums:
            numSum+=value
            if numSum<minNum:
                minNum=numSum
        return 1 if minNum>=1 else abs(minNum)+1
