
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next= next

class Solution:
    #head:类型，就是表明传入的这个参数的类型是什么，函数结束后箭头表示建议的返回值类型。
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        #没有节点的情况
        if head is None:
            node.next = node
            return node
        #只有一个头节点的情况
        if head.next == head:
            head.next = node
            node.next = head
            return head
        curr = head
        next = head.next
        while next != head:
            if curr.val <= insertVal <= next.val:
                break
            if curr.val > next.val:
                if insertVal > curr.val or insertVal < next.val:
                    break
            curr = curr.next
            next = next.next
        curr.next = node
        node.next = next
        return head