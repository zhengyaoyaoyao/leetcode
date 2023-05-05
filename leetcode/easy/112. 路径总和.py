# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from leetcode.medium.findFrequentTreeSum import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag=False
        def dfs(node,target):
            if node is None:
                return 0
            nonlocal  flag
            if node.left is None and node.right is None and target-node.val==0:
                flag=True
            dfs(node.left,target-node.val)
            dfs(node.right,target-node.val)
        dfs(root,targetSum)
        return flag