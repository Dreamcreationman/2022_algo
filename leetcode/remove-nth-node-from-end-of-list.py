# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/submissions/
        if not head: return
        node = ListNode(0)
        node.next = head
        slow = node
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return node.next
