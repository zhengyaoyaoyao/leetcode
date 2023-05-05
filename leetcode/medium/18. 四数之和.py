from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        if not nums or len(nums)<4:
            return ans
        for first in range(0,n-3):
            #避免重复,因为双指针会找到一组值，如果你前面重复了双指针可不会管你，所以相同要跳过。
            # 如果是num[first]==num[first+1]跳过的话，这样就让-1，-1，2这种情况跳过了。只剩下-1，2，因为我们是允许内部一样的。
            if first>0 and nums[first]==nums[first-1]:
                continue
            if nums[first]+nums[first+1]+nums[first+2]+nums[first+3]>target:
                break
            if nums[first]+nums[n-3]+nums[n-2]+nums[n-1]<target:
                #即这个first太小了，直接下一个
                continue
            for second in range(first+1,n-2):
                if second>first+1 and nums[second]==nums[second-1]:
                    continue
                if nums[first]+nums[second]+nums[second+1]+nums[second+2]>target:
                    break
                if nums[first]+nums[second]+nums[-1]+nums[-2]<target:
                    continue
                tar = target-(nums[first]+nums[second])
                four = n-1
                for third in range(second+1,n):
                    if third>second+1 and nums[third]==nums[third-1]:
                        continue
                    while third<four and nums[third]+nums[four]>tar:
                        four-=1
                    if third==four:
                        break
                    if nums[third]+nums[four]==tar:
                        ans.append([nums[first],nums[second],nums[third],nums[four]])
        return list(ans)
if __name__ == '__main__':
    nums=[2,2,2,2,2]
    test=Solution()
    target = 8
    print(test.fourSum(nums,target))