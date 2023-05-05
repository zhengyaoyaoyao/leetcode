# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
删除节点，倒数第几个，用快慢指针
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headNode  = ListNode()
        headNode.next = head
        fast = head
        slow = headNode
        while n>0:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            slow = slow.next
        # slow到达要删除的位置
        slow.next = slow.next.next
        return headNode.next

if __name__ == '__main__':
    node1 =  ListNode(1)
    n = 1
    test=Solution()
    test.removeNthFromEnd(node1,n)