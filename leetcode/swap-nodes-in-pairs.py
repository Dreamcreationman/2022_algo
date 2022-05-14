# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

    def swapPairs_two(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        newHead = head.next
        dummyHead = ListNode(0)
        dummyHead.next = head
        temp, node1, node2 = dummyHead, dummyHead.next, dummyHead.next.next
        while temp and node1 and node2:
            temp.next = node2
            node1.next = node2.next
            node2.next = node1

            temp = temp.next.next
            node1, node2 = temp.next, temp.next.next if temp.next else None
        return newHead


if __name__ == '__main__':
    import utils
    head = utils.create_linked_list([1, 2, 3, 4])
    sol = Solution()
    print(utils.print_linked_list(sol.swapPairs(head)))
