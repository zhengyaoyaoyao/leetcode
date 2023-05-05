#层序遍历。然后记录高度，找到左右都没孩子的就直接退出，最短路径上节点的数量就是高度
# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        if root is None:
            return 0
        deque = collections.deque()
        deque.append(root)
        while deque:
            layerNum = len(deque)
            ans += 1
            for  i in range(layerNum):
                node = deque.popleft()
                if node.left is None and node.right is None:
                    return ans
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

