from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:return 0
        q = deque()
        sum = 0
        q.append(root)
        while q:
            node = q.popleft()
            sum += 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return sum

    def countNodes_cur(self, root: TreeNode) -> int:
        if not root: return 0
        return self.countNodes_cur(root.left) + self.countNodes_cur(root.right) + 1

    def countNodes_cur_two(self, root: TreeNode) -> int:
        # https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/chang-gui-jie-fa-he-ji-bai-100de-javajie-fa-by-xia/
        if not root:return 0
        leftlevel = self.countLevels(root.left)
        rightlevel = self.countLevels(root.right)
        if leftlevel == rightlevel:
            return self.countNodes(root.right) + (1 << leftlevel)
        else:
            return self.countNodes(root.left) + (1 << rightlevel)

    def countLevels(self, node):
        if not node:
            return 0
        level = 0
        while node:
            level += 1
            node = node.left
        return level
