from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
        if not root: return []
        res, q = [], deque()
        q.append(root)
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(tmp)
        return res

    def levelOrder_two(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(root, depth):
            if depth == len(res):
                res.append([])  # start the current depth
            res[depth].append(root.val)  # fulfil the current depth
            # process the child nodes for the next depth
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)

        dfs(root, 0)
        return res

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
        if not root: return []
        q = deque()
        q.append(root)
        res = []
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(tmp)
        return res[::-1]
