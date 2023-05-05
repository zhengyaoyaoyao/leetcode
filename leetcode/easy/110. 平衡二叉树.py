# class TreeNode:
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=[True]
        def dfs(node):
            if node is None:
                return 0
            lefthight = dfs(node.left)
            righthight = dfs(node.right)
            if  abs(lefthight-righthight)>1:
                flag[0]=False
            return max(lefthight,righthight)+1
        dfs(root)
        return flag[0]


if __name__ == '__main__':
    node1= TreeNode(3)
    node2= TreeNode(9)
    node3= TreeNode(20)
    node4= TreeNode(15)
    node5= TreeNode(7)
    node1.left=node2
    node1.right=node3
    node3.left=node4
    node3.right=node5
    test = Solution()
    print(test.isBalanced(node1))