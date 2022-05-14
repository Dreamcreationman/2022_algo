from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # https://leetcode-cn.com/problems/linked-list-cycle/
        if not head: return False
        slow = fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False

    def detectCycle(self, head: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/linked-list-cycle-ii/
        if not head: return head
        slow = fast = head
        cycle = False
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                cycle = False
                break
            if slow == fast:
                cycle = True
                break
        if cycle:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return

    def findDuplicate(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/find-the-duplicate-number
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
