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

    def postorderTraversal_cur(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        if not root: return []
        self.postorderTraversal_cur(root.left)
        self.postorderTraversal_cur(root.right)
        self.res.append(root.val)
        return self.res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        if not root: return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.left: s.append(node.left)
            if node.right: s.append(node.right)
        return res[::-1]