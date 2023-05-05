# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        help=[0,0,-1]
        #maxCount, count, valueCur = 0, 0, -1
        #搜索树，所以前序遍历就是一个有序数组，然后找出众数
        res=list()
        def update(x):
            if x==help[2]:
                help[1]+=1
            else:
                help[1]=1
                help[2]=x
            if help[1]==help[0]:
                res.append(help[2])
            if help[1]>help[0]:
                help[0]=help[1]
                res.clear()
                res.append(help[2])
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            update(node.val)
            dfs(node.right)
        dfs(root)
        return res


if __name__ == '__main__':
    node1= TreeNode(1)
    node2= TreeNode(2)
    node1.right=node2
    test = Solution()
    print(test.findMode(node1))