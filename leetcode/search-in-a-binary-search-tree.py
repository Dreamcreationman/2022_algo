# Definition for a binary tree node.
import select


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
        if not root: return root
        while root:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
        return

    def searchBST_cur(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return
        if val == root.val: return root
        elif val < root.val: return self.searchBST_cur(root.left, val)
        else: return self.searchBST_cur(root.right, val)