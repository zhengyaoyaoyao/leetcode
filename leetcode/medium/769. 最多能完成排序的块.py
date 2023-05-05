'''
核心思路：从后往前遍历，用right和left去卡范围，范围内如果最小值大于前面的最大值，那么就可以断开。
'''
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 1
        left,right = len(arr)-1,len(arr)
        while left>0:
            if min(arr[left:right])>max(arr[:left]):
                ans+=1
                right=left
            left-=1
        return ans


