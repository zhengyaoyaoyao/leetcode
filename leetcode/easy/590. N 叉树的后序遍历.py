import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans =[]
        def dfs(node:'Node'):
            if node is None:
                return
            for ch in node.children:
                dfs(ch)
            ans.append(node.val)
        dfs(root)
        return ans

'''
迭代
'''
class Solution1:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = []
        nextIndex = collections.defaultdict(int)
        node = root
        while st or node:
            while node:
                st.append(node)
                if not node.children:
                    break
                nextIndex[node] = 1
                node = node.children[0]
            node = st[-1]
            i = nextIndex[node]
            if i < len(node.children):
                nextIndex[node] = i + 1
                node = node.children[i]
            else:
                ans.append(node.val)
                st.pop()
                del nextIndex[node]
                node = None
        return ans
'''
迭代优化
'''
class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        st = [root]
        vis = set()
        while st:
            node = st[-1]
            # 如果当前节点为叶子节点或者当前节点的子节点已经遍历过
            if len(node.children) == 0 or node in vis:
                ans.append(node.val)
                st.pop()
                continue
            st.extend(reversed(node.children))
            vis.add(node)
        return ans
