
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left =left
        self.right = right

class Solution:
    def largestValues(self, root) :
        if root is None:
            return []
        queue = [root]
        ans =[]
        i=1
        p=1
        while queue:
            maxVal = (-2)**31
            tem =queue
            queue=[]
            for node in tem:
                maxVal=max(maxVal,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(maxVal)
        return ans


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(5)
    node5 = TreeNode(3)
    node6 = TreeNode(9)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.right=node6
    test = Solution()
    print(test.largestValues(node1))