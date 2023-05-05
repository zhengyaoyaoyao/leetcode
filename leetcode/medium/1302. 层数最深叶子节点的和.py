# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #先进行层序遍历
        queue = collections.deque()
        queue.append(root)
        while queue:
            numSum=0
            layer = len(queue)
            for _ in range(layer):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                numSum+=node.val

        return numSum

