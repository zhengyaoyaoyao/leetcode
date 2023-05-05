import collections
from typing import List

'''
暴力解，超时
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count= 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        if nums1[i]+nums2[j]+nums3[k]+nums4[l]==0:
                            count+=1
        return count

'''
哈希加分组
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        countAB = collections.Counter(i+j for i in nums1 for j in nums2)
        ans = 0
        for k in nums3:
            for l in nums4:
                if -k-l in countAB:
                    ans+=countAB[-k-l]
        return ans
