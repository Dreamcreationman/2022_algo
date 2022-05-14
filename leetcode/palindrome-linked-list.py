from utils import create_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # https://leetcode-cn.com/problems/palindrome-linked-list
        if head is None: return True
        q = []
        phead = head
        while phead:
            q.append(phead.val)
            phead = phead.next
        phead = head
        while phead:
            if phead.val != q.pop():
                return False
            phead = phead.next
        return True

    def isPalindrome_ii(self, head: ListNode) -> bool:
        if head is None: return True
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        pslow = slow.next
        pre = self.reverse_list(pslow)
        phead = head
        ppre = pre
        while ppre:
            if phead.val != ppre.val: return False
            ppre = ppre.next
            phead = phead.next
        slow.next = self.reverse_list(pre)
        return True

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome_ii(create_linked_list([1,2, 2, 1])))