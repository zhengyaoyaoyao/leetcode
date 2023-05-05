class ListNode:
    def __int__(self,val):
        self.val = val
        self.next= None


class MyLinkedList:
    '''
    最好需要一个哨兵作为头节点，然后size记录有效长度，这样会方便后面很多
    '''
    def __init__(self):
        self.length = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index<0 or index>=self.length:
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.length:
            return
        # 这样扩大了兼容性，反正负的你都是在头加，方便了上面在头加节点的函数。
        index = max(0,index)
        self.length+=1
        p = self.head
        # 因为index是第几个，从1开始，但是length是从0开始，所以本身就会少一个，所以往后遍历index次就到了pred的地方。
        for _ in range(index):
            p = p.next
        to_added = ListNode(val)
        to_added.next = p.next
        p.next = to_added

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.length:
            return
        self.length-=1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next



