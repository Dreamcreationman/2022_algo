from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/
        if not root: return False
        q = deque()
        q.append(root)
        leaf = False
        while q:
            node = q.popleft()
            left = node.left
            right = node.right
            if (leaf and (left or right)) or ((not left) and right):
                return False
            if left: q.append(left)
            if right: q.append(right)
            if not left or not right:
                leaf = True
        return True
