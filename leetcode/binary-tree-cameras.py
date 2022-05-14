import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node):

        if not node: return math.inf, 0, 0
        la, lb, lc = self.helper(node.left)
        ra, rb, rc = self.helper(node.right)
        a = lc + rc + 1
        b = min(a, la + rb, lb + ra)
        c = min(a, lb + rb)
        return a, b, c

    def minCameraCover(self, root: TreeNode) -> int:
        # https://leetcode-cn.com/problems/binary-tree-cameras/
        if not root: return 0
        a, b, c = self.helper(root)
        return b