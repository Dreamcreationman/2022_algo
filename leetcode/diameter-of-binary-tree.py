# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, node):
        if not node: return [0, 0]
        maxLeftDis, leftHeight = self.helper(node.left)
        maxRightDis, rightHeight = self.helper(node.right)
        maxDis = max(maxLeftDis, maxRightDis, leftHeight + rightHeight + 1)
        maxHeight = max(leftHeight, rightHeight) + 1
        return maxDis, maxHeight

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # https://leetcode-cn.com/problems/diameter-of-binary-tree
        if not root: return 0
        maxDis, _ = self.helper(root)
        return maxDis - 1