# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        headNum = ListNode(0)
        headNum.next= head
        p = headNum
        while p.next and p.next.next:
            q = p.next
            r = p.next.next
            p.next = r
            q.next = r.next
            r.next =q
            p=q
        return headNum.next
