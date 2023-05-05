from typing import List


class Solution:
    #建立字典判断是否有在字典中的。
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans ={}
        for i in nums:
            if i not in ans:
                ans[i]=1
            else:
                return True
        else:
            return False

    def containsDuplicate1(self, nums: List[int]) -> bool:
        '''直接利用集合的特性，所有元素添加进去，如果长度一样那就是没重复.'''
        return len(nums) != len(set(nums))