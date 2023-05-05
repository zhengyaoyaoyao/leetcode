import collections
from typing import List
'''
层序遍历转中序遍历
'''
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
'''
递归版本
'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node:'Node'):
            if node is None :
                return
            ans.append(node.val)
            for ch in node.children:
                dfs(ch)
        dfs(root)
        return ans

'''
非递归版本
'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans = []
        stack=[]
        nextIndex=collections.defaultdict(int)
        node = root
        # 栈非空或者node节点不是空
        while stack or node:
            while node:
                ans.append(node.val)
                stack.append(node)
                if not node.children:
                    break
                nextIndex[node]=1
                node = node.children[0]
            node=stack[-1]
            i = nextIndex[node]
            if i<len(node.children):
                nextIndex[node]=i+1
                node = node.children[i]
            else:
                stack.pop()
                del nextIndex[node]
                node=None
        return ans


'''
迭代优化，也是非递归，但是简化代码
'''
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        ans =[]
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(reversed(node.children))
        return ans




