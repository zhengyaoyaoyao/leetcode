# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def heightCul(root:Optional[TreeNode])->int:
            #先拿到树的高，层序遍历
            deque = collections.deque()
            deque.append(root)
            layer = -1
            while deque:
                layer+=1
                number = len(deque)
                for _ in range(number):
                    node = deque.popleft()
                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
            return layer
        #得到树的高layer
        height = heightCul(root)
        m = height+1
        n = 2** m -1
        #构建出这个矩阵
        res = [[""]*n for _ in range(m)]
        q = collections.deque([(root,0,(n-1)//2)])
        while q:
            node ,r,c = q.popleft()
            res[r][c] = str(node.val)
            if node.left:
                q.append((node.left,r+1,c-2 ** (height-r-1)))
            if node.right:
                q.append((node.right,r+1,c+2 **(height-r-1)))
        return res