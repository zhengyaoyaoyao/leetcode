import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #时间复杂度：O（n）
    #空间复杂度：O（n）
    def isPalindrome(self, head: ListNode) -> bool:
        queue = collections.deque()
        while head:
            queue.append(head.val)
            head = head.next
        left = 0
        right = len(queue)-1
        while left<right:
            if not (queue[left] == queue[right]):
                return False
            left+=1
            right-=1
        return True

    #再python语法层上的优化，也是利用列表
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        #python中能够直接让vals向后遍历，直接让他看是否相等于倒着切片。牛。
        return vals ==vals[::-1]

    #不用列表，在原地进行，那么就是使用快慢指针，做题的时候也想到了从中间开始，那么就要分单双数，然后进行转置。
class Solution2:
    def isPalindrome(self,head:ListNode) ->bool:
        if head is None:
            return True
        #找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        #判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position =first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next=self.reverse_list(second_half_start)
        return result


    def end_of_first_half(self,head):
        fast = head
        slow = head
        while fast.next.next is not None and slow.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self,head):
        previous =None
        current=head
        while current is not None:
            next_node = current.next
            current.next=previous
            previous=current
            current = next_node
        return previous
