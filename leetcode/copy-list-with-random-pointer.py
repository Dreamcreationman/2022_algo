# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # https://leetcode-cn.com/problems/copy-list-with-random-pointer/
        if not head: return
        dic = {}
        phead = head
        while phead:
            dic[phead] = Node(phead.val)
            phead = phead.next
        phead = head
        while phead:
            dic[phead].next = dic.get(phead.next)
            dic[phead].random = dic[phead.random] if phead.random is not None else None
            phead = phead.next
        return dic[head]

    def copyRandomList_ii(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        phead = head
        while phead:
            temp = Node(phead.val)
            temp.next = phead.next
            phead.next = temp
            phead = temp.next
        phead = head
        while phead:
            phead.next.random = phead.random.next if phead.random else None
            phead = phead.next.next
        phead = head
        copiedHead = Node(-1)
        pcopied = copiedHead
        while phead:
            pcopied.next = phead.next
            pcopied = pcopied.next
            phead.next = pcopied.next
            phead = phead.next
        return copiedHead.next


if __name__ == '__main__':
    sol = Solution()
    sol.copyRandomList_ii()