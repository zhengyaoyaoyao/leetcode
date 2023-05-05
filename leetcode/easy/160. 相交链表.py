# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node1 = headA
        node2 = headB
        while node1.next:
            node1= node1.next
        while node2.next:
            node2 = node2.next
        if node1 !=node2:
            return None
        n= 0
        node1 = headA
        node2 = headB
        while node1.next:
            node1 = node1.next
            n+=1
        while node2.next:
            node2 = node2.next
            n-=1
        if n>0:
            moreLength = headA
            moreShort = headB
        else:
            moreLength = headB
            moreShort = headA
        n = abs(n)
        while n>0:
            moreLength=moreLength.next
            n-=1
        while moreLength!=moreShort:
            moreLength=moreLength.next
            moreShort=moreShort.next
        return moreLength




