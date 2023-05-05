from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [0] * n
        nums1.sort()  # nums1是可以排序的
        ids = sorted(range(n), key=lambda i: nums2[i])
        left, right = 0, n - 1
        for x in nums1:
            if x > nums2[ids[left]]:
                ans[ids[left]] = x
                left+=1
            else:
                ans[ids[right]] = x
                right -= 1
        return ans


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    test = Solution()
    print(test.advantageCount(nums1, nums2))
