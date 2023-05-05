from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for i in nums2:
            if i in nums1:
                ans.add(i)
        return list(ans)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def intersection(set1,set2):
            return [x for x in set1 if x in set2]
        set1 = set(nums1)
        set2 = set(nums2)
        return intersection(set1,set2)
