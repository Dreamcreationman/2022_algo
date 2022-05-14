# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/linked-list-cycle-lcci/
        if not head: return head
        slow = fast = head
        while slow and fast:
            if slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
