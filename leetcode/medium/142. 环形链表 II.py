# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head.next
        quick=head.next.next
        #跳出的时候停的位置就是slow和quick相同的位置
        while slow !=quick:
            if quick.next is None or quick.next.next is None:
                return None
            slow=slow.next
            quick=quick.next.next
        quick=head
        while quick !=slow:
            quick= quick.next
            slow = slow.next
        return slow

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        check  =set()
        p = head
        while p:
            if p in check:
                return p
            else:
                check.add(p)
                p = p.next