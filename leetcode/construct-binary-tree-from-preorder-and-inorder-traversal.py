from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder, inorder):
            if preorder == []:
                return
            dic = {}
            for idx, d in enumerate(inorder):
                dic[d] = idx
            root = TreeNode(preorder[0])
            inleft = inorder[:dic[preorder[0]]]
            preleft = preorder[1:dic[preorder[0]]+1]
            inright = inorder[dic[preorder[0]]+1:]
            preright = preorder[dic[preorder[0]]+1:]
            left = helper(preleft, inleft)
            right = helper(preright, inright)
            root.left = left
            root.right = right
            return root
        root = helper(preorder, inorder)
        return root


if __name__ == '__main__':
    sol = Solution()
    print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))
