from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
关键，设置一个新的链表，然后对原本的遍历的链表进行头插法
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q= ListNode()
        # 开始遍历旧的链表
        p = head
        while p:
            node = ListNode(p.val)
            node.next=q.next
            q.next = node
            p = p.next
        return q.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre
