# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dummyA = ListNode()
        dummyA.next = headA
        dummyB = ListNode()
        dummyB.next = headB
        lenA = 0
        while headA:
            lenA+=1
            headA=  headA.next
        lenB = 0
        while headB:
            lenB+=1
            headB= headB.next
        # 计算出两个长度后做差
        dis = lenA-lenB
        headA = dummyA.next
        headB = dummyB.next
        if dis>0:
            # 大于0就是A更长。
            while dis!=0:
                dis-=1
                headA=  headA.next
            while headA and headB:
                if id(headA)==id(headB):
                    return headA
                headB= headB.next
                headA= headA.next
            if headA is None:
                return None
        else:
            while dis!=0:
                dis+=1
                headB  = headB.next
            while headA and headB:
                if id(headA)==id(headB):
                    return headA
                headB= headB.next
                headA= headA.next
            if headA is None:
                return None

'''
使用双指针进行移动
其实不用一起往下走，可以一个链表走到后面后再让下一个链表开始移动
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while id(pA) != id(pB):
            # 这里面有多次的遍历操作，不断地循环，直到两个一起到了None。
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA