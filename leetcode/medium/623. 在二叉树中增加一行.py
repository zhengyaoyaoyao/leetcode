import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val,left=root)
        #先是一个层序遍历的模板，但是只需要到depth-1层
        queue = collections.deque()
        queue.append(root)
        layer = 1
        while queue:
            layerNum = len(queue)
            for _ in range(layerNum):
                node = queue.popleft()
                if layer == depth-1:
                    nodeLeft =TreeNode(val,left=node.left)
                    node.left=nodeLeft
                    nodeRight = TreeNode(val,right=node.right)
                    node.right = nodeRight
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            layer+=1
        return root

'''官方简洁答案。直接遍历到那层就行。就是遍历depth-1次，然后在那层的节点处操作。'''
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)
        curLevel = [root]
        for _ in range(1, depth - 1):
            tmpt = []
            for node in curLevel:
                if node.left:
                    tmpt.append(node.left)
                if node.right:
                    tmpt.append(node.right)
            curLevel = tmpt
        for node in curLevel:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root
