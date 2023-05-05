from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if nums[-1] - n == 0:
            return [nums[-1] + 1, nums[-1] + 2]
        elif nums[-1] - n == 1:
            # 这种情况一个在前一个在后,只要找到前面那个就行。
            if nums[0] != 1:
                return [1, nums[-1] + 1]
            else:
                for i in range(n - 1):
                    if nums[i + 1] - nums[i] != 1:
                        return [nums[i] + 1, nums[-1] + 1]
        else:
            hashSet = set()
            if n ==1:
                return [1,2]
            # 这种情况就是两个都在前面
            for i in range(n - 1):
                if len(hashSet) == 2:
                    return list(hashSet)
                if i ==0 and nums[0] != 1:
                    hashSet.add(1)
                    if nums[0] !=2:
                        hashSet.add(2)
                if nums[i + 1] - nums[i] == 3:
                    hashSet.add(nums[i]+1)
                    hashSet.add(nums[i]+2)
                if nums[i + 1] - nums[i] == 2:
                    hashSet.add(nums[i] + 1)
            return list(hashSet)


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        #运用数学的解法，因为是由连续的数字，所以可以求N个的总和和M个的总和。通过差值就能够计算出两个的总和，然后总和//2就是分布在两侧
        n = len(nums)+2
        cur = n*(1+n)//2 -sum(nums)
        tot, mid =cur, cur//2
        cur=  mid*(mid+1)//2 - sum([x for x in nums if x<=mid])
        return [cur,tot-cur]
if __name__ == '__main__':
    nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    test = Solution()
    print(test.missingTwo(nums))
    # set={1,2}
    # print(list(set))