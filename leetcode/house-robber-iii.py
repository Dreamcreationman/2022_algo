# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def helper(self, node):
        if not node: return 0, 0
        maxRobLeft, maxNotRobLeft = self.helper(node.left)
        maxRobRight, maxNotRobRight = self.helper(node.right)
        maxRob = node.val + maxNotRobLeft + maxNotRobRight
        maxNotRob = 0 + max(maxRobLeft, maxNotRobLeft) + max(maxRobRight, maxNotRobRight)
        return maxRob, maxNotRob

    def rob(self, root: TreeNode) -> int:
        # https://leetcode-cn.com/problems/house-robber-iii
        if not root: return 0
        return max(self.helper(root))