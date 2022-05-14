from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, q = [], collections.deque()
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
            else:
                res.append(tmp[::-1])
            level += 1
        return res

    def levelOrder_two(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        res = []
        dic = {}
        dic[root] = 1
        curlevel = 1
        tmp = []
        while q:
            node = q.popleft()
            curnodeLevel = dic[node]
            if curnodeLevel == curlevel:
                tmp.append(node.val)
            else:
                res.append(tmp)
                tmp = []
                tmp.append(node.val)
                curlevel += 1
            if node.left:
                q.append(node.left)
                dic[node.left] = curnodeLevel + 1
            if node.right:
                q.append(node.right)
                dic[node.right] = curnodeLevel + 1
        res.append(tmp)
        return res