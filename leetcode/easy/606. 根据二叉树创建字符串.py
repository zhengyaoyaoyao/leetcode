# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def dfs(node):
            if node is None:
                return None
            ans.append(node.val)
            if node.left:
                ans.append('(')
                dfs(node.left)
                ans.append(')')
            elif node.right:
                ans.append('()')
            if node.right:
                ans.append('(')
                dfs(node.right)
                ans.append(')')
        dfs(root)
        res=''
        for i in ans:
            res+=str(i)
        return res