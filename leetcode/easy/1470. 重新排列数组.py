from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0]*(2*n)
        left = 0
        right= n
        for i in range(n):
            ans[2*i]=nums[left]
            ans[2*i+1] = nums[right]
            left+=1
            right+=1
        return ans