# class TreeNode:
import collections
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #如果两个都不存在
        if not p and not q:
            return True
        #如果有一个不存在一个存在
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        #如果都存在，并且值也相同了，往下走
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


