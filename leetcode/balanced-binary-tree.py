# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/balanced-binary-tree/
        def helper(node):
            if not node:
                return [True, 0]
            lbalanced, lheight = helper(node.left)
            rbalanced, rheight = helper(node.right)
            height = max(lheight, rheight) + 1
            balanced = lbalanced and rbalanced and abs(lheight - rheight) < 2
            return balanced, height
        b, h = helper(root)
        return b