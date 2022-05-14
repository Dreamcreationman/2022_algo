from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal_cur(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode-cn.com/problems/binary-tree-preorder-traversal/submissions/
        if not root: return []
        self.res.append(root.val)
        self.preorderTraversal_cur(root.left)
        self.preorderTraversal_cur(root.right)
        return self.res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res =  []
        s = []
        s.append(root)
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right: s.append(node.right)
            if node.left: s.append(node.left)
        return self.res

    def preorderTraversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        cur = root
        res = []
        while cur:
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right

                if not mostRight.right:
                    res.append(cur.val)
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
            else:
                res.append(cur.val)
            cur = cur.right
        return res