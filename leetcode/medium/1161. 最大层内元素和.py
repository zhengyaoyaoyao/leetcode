#树的层序遍历
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        laySum=[]
        maxNum= float('-inf')
        while len(queue) != 0:
            layerSum = 0
            layerNum = len(queue)
            for _ in range(layerNum):
                CurNode = queue.popleft()
                layerSum+=CurNode.val
                if CurNode.left != None:
                    queue.append(CurNode.left)
                if CurNode.right !=None:
                    queue.append(CurNode.right)
            maxNum = max(maxNum,layerSum)
            laySum.append(layerSum)
        res =[index+1 for index,x in enumerate(laySum) if x == maxNum]
        return res[0]

if __name__ == '__main__':
    node1= TreeNode(1)
    node2= TreeNode(7)
    node3= TreeNode(0)
    node4= TreeNode(7)
    node5= TreeNode(-8)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    test = Solution()
    print(test.maxLevelSum(node1))