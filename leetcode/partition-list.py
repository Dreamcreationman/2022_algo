from utils import create_linked_list, print_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # https://leetcode-cn.com/problems/partition-list/
        smallHead = None
        smallTail = None
        bigHead = None
        bigTail = None

        phead = head
        while phead:
            next = phead.next
            phead.next = None
            if phead.val < x:
                if smallHead is None:
                    smallHead = phead
                    smallTail = phead
                else:
                    smallTail.next = phead
                    smallTail = phead
            else:
                if bigHead is None:
                    bigHead = phead
                    bigTail = phead
                else:
                    bigTail.next = phead
                    bigTail = phead
            phead = next
        if smallHead is not None:
            smallTail.next = bigHead
        else:
            return bigHead
        return smallHead


if __name__ == '__main__':
    sol = Solution()
    print(print_linked_list(sol.partition(create_linked_list([1]), 0)))