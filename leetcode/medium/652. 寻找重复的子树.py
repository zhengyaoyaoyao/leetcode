# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            tri = (node.val, dfs(node.left), dfs(node.right))
            if tri in seen:
                (tree, index) = seen[tri]
                repeat.add(tree)
                return index
            else:
                nonlocal idx
                idx += 1
                seen[tri] = (node, idx)
                return idx

        idx = 0
        seen = dict()
        repeat = set()

        dfs(root)
        return list(repeat)


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen  = dict()
        repeat = set()
        def dfs(node:TreeNode)->str:
            if node is None:
                return ""
            serial = "".join([str(node.val),"(",dfs(node.left),")",dfs(node.right),")"])
            if serial in seen.keys():
                repeat.add(seen[serial])
            else:
                seen[serial]=node
            return serial
        dfs(root)
        return list(repeat)
