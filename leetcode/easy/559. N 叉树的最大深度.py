import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        queue=[root]
        layer = 0
        while queue:
            queue=[child for node in queue for child in node.children]
            layer +=1
        return layer

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        queue=collections.deque()
        queue.append(root)
        layer = 0
        while queue:
            layerNum = len(queue)
            for i in range(layerNum):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            layer +=1
        return layer