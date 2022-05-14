from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://leetcode-cn.com/problems/rotate-list/
        if not head: return head
        phead, n = head, 0
        while phead:
            phead = phead.next
            n += 1
        k %= n
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = head
        newhead = slow.next
        slow.next = None
        return newhead

    def rotateRight_two(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://leetcode-cn.com/problems/rotate-list/
        if not head: return head
        phead, n = head, 1
        newhead = phead
        while phead.next:
            phead = phead.next
            n += 1
        k = n - k % n
        phead.next = head
        while k > 1:
            newhead = newhead.next
            k -= 1
        res = newhead.next
        newhead.next = None
        return res