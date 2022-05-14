# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
        if not headA and not headB: return
        pa, pb = headA, headB
        lena = lenb = 0
        while pa:
            pa = pa.next
            lena += 1
        while pb:
            pb = pb.next
            lenb += 1
        lens = lenb - lena
        if pa != pb: return
        pa, pb = headA, headB
        if lens > 0:
            while pa != pb:
                while lens != 0:
                    pb = pb.next
                    lens -= 1
                if pa == pb: return pa
                pb = pb.next
                pa = pa.next
        else:
            lens = -lens
            while pa != pb:
                while lens != 0:
                    pa = pa.next
                    lens -= 1
                if pa == pb: return pa
                pb = pb.next
                pa = pa.next
        return pa

    def getIntersectionNode_two(self, headA: ListNode, headB: ListNode) -> ListNode:
        # https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
        """
        两者在同为空的时候 表示都走到了最末尾的空节点（长度的公倍数）
        否者就是走到了有公共节点的位置
        :param headA:
        :param headB:
        :return:
        """
        if not headA and not headB: return
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa

"""不存在一个链表有环，另一个链表无环的单链表相交情况"""