from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoList_recur(self, heada, headb):
        if not heada: return headb
        if not headb: return heada
        if heada.val < headb.val:
            heada.next = self.mergeTwoList_recur(heada.next, headb)
            return heada
        else:
            headb.next = self.mergeTwoList_recur(heada, headb.next)
            return headb

    def mergeTwoList(self, heada, headb):
        pheada, pheadb = heada, headb
        newHead = ListNode(0)
        pnewhead = newHead
        while pheada and pheadb:
            if pheada.val < pheadb.val:
                pnewhead.next = pheada
                pnewhead = pnewhead.next
                pheada = pheada.next
            else:
                pnewhead.next = pheadb
                pnewhead = pnewhead.next
                pheadb = pheadb.next
        pnewhead.next = pheada if pheada else pheadb
        return newHead.next

    def merge(self, nodelist, l, r):
        if l == r: return nodelist[l]
        m = l + ((r - l) >> 1)
        l1 = self.merge(nodelist, l, m)
        l2 = self.merge(nodelist, m + 1, r)
        return self.mergeTwoList(l1, l2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [[]]:
            return
        return self.merge(lists, 0, len(lists) - 1)
