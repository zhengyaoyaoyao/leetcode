# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #先前序遍历就可以得到原来的数组，然后把5加入到末尾。然后再构造一次。
        old = []
        def dfs(node:Optional[TreeNode]):
            if node is None:
                return
            if node.left:
                dfs(node.left)
            old.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        old.append(val)
        def Construct(left,right):
            if left>right:
                return None
            maxIndex = left
            for i in range(left+1,right+1):
                if old[i]>old[maxIndex]:
                    maxIndex=i
            #找到最大值然后开始遍历
            node = TreeNode(old[maxIndex])
            node.left=Construct(left,maxIndex-1)
            node.right= Construct(maxIndex+1,right)
            return node
        return Construct(0,len(old)-1)

if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    node1.left=node2
    node1.right=node3
    node3.left=node4
    test = Solution()
    print()
