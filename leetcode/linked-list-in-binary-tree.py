class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, query, node):
        if not query: return True
        if not node: return False
        if query.val != node.val:
            return False
        return self.dfs(query.next, node.right) or self.dfs(query.next, node.left)

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/linked-list-in-binary-tree
        if not root: return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)