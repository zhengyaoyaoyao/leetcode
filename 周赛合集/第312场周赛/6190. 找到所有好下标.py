from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        def dec(checkNums):
            for index in range(len(checkNums) - 1):
                if checkNums[index + 1] > checkNums[index]:
                    return False
            return True

        def up(checkNums):
            for index in range(len(checkNums) - 1):
                if checkNums[index + 1] < checkNums[index]:
                    return False
            return True

        # 先花时间做一个排除，如果前后不是递增递减的就不要了。
        for i in range(1, len(nums) - 1):
            if nums[i - 1] > nums[i] or nums[i + 1] < nums[i]:
                nums[i] = -1
        ans = []
        for i in range(k, len(nums) - k):
            if nums[i] > 0 and dec(nums[i - k:i]) and up(nums[i + 1:i + k + 1]):
                ans.append(i)
        return ans


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # just =>子数组
        # 拆分成左右两个问题
        # 左边统计非递增的子数组的最长长度，只要k小于当前的值，那么就是说明左边比它小的还够
        # 右边统计非递增的子数组的最长长度，只要k小于当前的值，那么久说明右边比它小的还有
        # 递推
        n = len(nums)
        ans = []
        dp = [1] * n
        for i in range(n - 2, k, -1):
            if nums[i] <= nums[i + 1]:
                dp[i] = dp[i + 1] + 1
        # 上面这样就统计好了从后往前有多少个非递增子数组
        inc = 1 #inc相当于统计了前面有多少个，就同步的进行了。
        for i in range(1, n - k):
            if inc >= k and dp[i + 1] >= k:
                ans.append(i)
            if nums[i - 1] >= nums[i]:
                inc += 1
            else:
                inc = 1
        return ans
