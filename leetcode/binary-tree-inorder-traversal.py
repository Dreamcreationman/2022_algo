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

    def inorderTraversal_cur(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
        if not root: return []
        self.inorderTraversal_cur(root.left)
        self.res.append(root.val)
        self.inorderTraversal_cur(root.right)
        return self.res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        s = []
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        cur = root
        res = []
        while cur:
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right

                if not mostRight.right:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None

            res.append(cur.val)
            cur = cur.right
        return res