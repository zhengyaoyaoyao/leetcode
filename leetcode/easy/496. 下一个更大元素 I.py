from typing import List


class Solution:
    #时间复杂度：O（m*n）
    #空间复杂度O（n）
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            flag=False
            for index,j in enumerate(nums2):
                if i == j:
                    flag=True
                if j>i and flag:
                    ans.append(j)
                    break
                if index==len(nums2)-1:
                    ans.append(-1)
        return ans
    #代码优化,思路一致
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n  = len(nums1),len(nums2)
        res=[0]*m
        for i in range(m):
            j = nums2.index(nums1[i])
            k=j+1
            while k<n and nums2[k]<nums2[i]:
                k+=1
            res[i] = nums2[k] if k<n else -1
        return res

    #使用单调栈+哈希表
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #用来保存结果
        res={}
        # 单调栈
        stack = []
        for num in reversed(nums2):
            # 栈不为空，并且当前的数字大于栈顶元素
            while stack and num >= stack[-1]:
                # 如果栈里面没有比我大的，即都是比我小的，那么全弹出
                # 没弹出的那个就是比我大的。
                stack.pop()
            # 没弹出的那个就是比我大的，如果栈是空的意思就是没有比我大的，那么就是-1，栈有东西，那么栈顶就是比我大的.
            res[num]=stack[-1] if stack else -1
        # 直接去里面拿结果就行。结果集就是res
        return [res[num] for num in nums1]

