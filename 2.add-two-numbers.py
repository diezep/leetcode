#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        heap = None
        nxt = None
        carry = 0
        while l1 is not None or l2 is not None:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            summ = (n1 + n2 + carry)
            carry = summ // 10

            if heap is None:
                heap = ListNode(summ% 10)
                nxt = heap
            else:
                nxt.next = ListNode(summ% 10)
                nxt = nxt.next
            
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        if carry:
            nxt.next = ListNode(1)

        return heap
# @lc code=end