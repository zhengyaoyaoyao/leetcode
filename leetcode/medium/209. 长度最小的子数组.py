from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        left ,right= 0,0
        check = 0
        while right< len(nums):
            if check<target:
                check+=nums[right]
                right+=1
            while check>=target:
                ans = min(ans,right-left)
                check-=nums[left]
                left+=1
        return ans if ans!=len(nums)+1 else 0


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 边界判断
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        # i为起始位置，j为结束位置。
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                # 满足时更新最小长度的位置。
                if total >= s:
                    ans = min(ans, j - i + 1)
                    break
        # 这个判断是为了防止永远不满足总和≥target的情况，此时返回0
        return 0 if ans == n + 1 else ans

if __name__ == '__main__':
    target = 7
    numps = [2,3,1,2,4,3]
    test = Solution()
    print(test.minSubArrayLen(target, numps))