from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q  = deque()
        res = []
        q.append(root)
        level = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if level % 2 == 0:
                res.append(tmp)
            else: res.append(tmp[::-1])
            level += 1
        return res