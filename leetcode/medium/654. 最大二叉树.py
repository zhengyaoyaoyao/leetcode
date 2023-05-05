# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left,right):
            # 递归出口
            if left>right:
                return None
            best = left
            #找到最大值的下标
            for i in range(left+1,right+1):
                if nums[i]>nums[best]:
                    best = i
            #创建这个节点，然后再左边右边递归重复
            node=TreeNode(nums[best])
            node.left = construct(left,best-1)
            node.right = construct(best+1,right)
            #递归的承接是一个节点，所以要返回这个节点。
            return node
        return construct(0,len(nums)-1)

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def layer(left,right):
            if left>right:
                return None
            median = nums[left,right+1].index(max(nums[left,right+1]))
            node = TreeNode(max(nums[left,right]))
            node.left=layer(left,median-1)
            node.right = layer(median+1,right)
            return node
        return layer(0,len(nums))


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent,cur = None,root
        while cur:
            if val>cur.val:
                #这里就是如果是最大值
                if not parent:
                    return TreeNode(val,root,None)
                #这里就是第三种情况，不大不小时
                node = TreeNode(val,cur,None)
                parent.right = node
                return root
            else:
                #这里就体现出只遍历右节点
                parent = cur
                cur = cur.right
        # 防止根节点为空时
        parent.right = TreeNode(val)
        return root




