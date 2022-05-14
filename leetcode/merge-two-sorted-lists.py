from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode-cn.com/tag/linked-list/problemset/
        pa, pb = list1, list2
        head = ListNode(0)
        phead = head
        while pa and pb:
            if pa.val < pb.val:
                phead.next = pa
                pa = pa.next
            else:
                phead.next = pb
                pb = pb.next
            phead = phead.next
            while pa:
                phead.next = pa
                phead = phead.next
                pa = pa.next
            while pb:
                phead.next = pb
                phead = phead.next
                pb = pb.next
            return head.next