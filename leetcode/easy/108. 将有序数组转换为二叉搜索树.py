#通过列表构建一个二叉树
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left,right):
            if left>right:
                return None
            mid = (left+right)>>1
            node = TreeNode(val=nums[mid])
            node.left=dfs(left,mid-1)
            node.right=dfs(mid+1,right)
            return node
        return dfs(0,len(nums)-1)

if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    test=Solution()
    test.sortedArrayToBST(nums)