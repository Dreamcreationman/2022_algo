import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ResType:
    def __init__(self, valid, mini, maxi):
        self.valid = valid
        self.mini = mini
        self.maxi = maxi


class Solution:
    def __init__(self):
        self.pre = -math.inf

    def isValidBST_cur(self, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/validate-binary-search-tree/
        if not root: return True
        left = self.isValidBST_cur(root.left)
        if not left: return False
        if root.val < self.pre:
            return False
        else:
            self.pre = root.val
        return self.isValidBST_cur(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        # https://leetcode-cn.com/problems/validate-binary-search-tree/
        if not root: return True
        s = []
        pre = -math.inf
        while s or root:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                if root.val <= pre:
                    return False
                else:
                    pre = root.val
                root = root.right
        return True

    def isValidBST_two(self, root: TreeNode) -> bool:
        def helper(node):
            if not node: return
            left = helper(node.left)
            right = helper(node.right)

            mini = node.val
            maxi = node.val
            if left:
                mini = min(mini, left.mini)
                maxi = max(maxi, left.maxi)
            if right:
                mini = min(mini, right.mini)
                maxi = max(maxi, right.maxi)    
            valid = True

            if left and (not left.valid or left.maxi >= node.val):
                valid = False
            if right and (not right.valid or right.mini <= node.val):
                valid = False
            return ResType(valid, mini, maxi)
        return helper(root).valid

    def isValidBST_morris(self, root: TreeNode) -> bool:
        if not root: return True
        cur = root
        pre = -math.inf
        while cur:
            mostRight = cur.left
            if mostRight:
                while mostRight.right and mostRight.right != cur:
                    mostRight = mostRight.right

                if not mostRight.right:
                    mostRight.right = cur
                    cur = cur.left
                    continue
                else:
                    mostRight.right = None
            if cur.val <= pre:
                return False
            else:
                pre = cur.val
            cur = cur.right
        return True