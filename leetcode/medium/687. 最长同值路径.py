# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        #为了后续的不断更新
        ans = 0
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left+1 if node.left and node.left.val == node.val else 0
            right1 = right+1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans,left1+right1)
            return max(left1,right1)
        dfs(root)
        return ans


