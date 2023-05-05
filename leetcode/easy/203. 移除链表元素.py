from typing import Optional

'''
关键在设置一个头节点，这样对于第一个节点的判断不用单独拿出来。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        q = ListNode()
        q.next=head
        head = q
        while q.next:
            if q.next.val ==val:
                q.next = q.next.next
            else:
                q = q.next
        return head.next

