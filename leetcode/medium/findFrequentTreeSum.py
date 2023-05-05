from collections import Counter


class TreeNode:
    def __init__(self,val = 0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def findFrequentTreeSum(self, root: TreeNode) :
        cnt = Counter()
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[sum] += 1
            return sum
        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]

