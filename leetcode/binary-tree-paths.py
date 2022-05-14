from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        paths = []

        def construct(node, path):
            if not node: return
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += "->"
                construct(node.left, path)
                construct(node.right, path)

        construct(root, "")
        return paths