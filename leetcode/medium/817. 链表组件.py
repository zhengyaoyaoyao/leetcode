# Definition for singly-linked list.
from collections import defaultdict
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans = 0
        check = set(nums)
        while head:
            if head.val in check:
                while head and head.val in check:
                    head = head.next
                ans += 1
            else:
                head = head.next
        return ans

