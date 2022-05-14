# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/reverse-linked-list/
        if not head: return
        pre, curr = None, head
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # https://leetcode-cn.com/problems/reverse-linked-list-ii
        if not head or left == right: return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        cur = pre.next
        for _ in range(right - left):
            nex = cur.next
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
        return dummy.next