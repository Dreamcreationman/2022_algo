from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#_"
        res = str(root.val) + "_"
        res += self.serialize(root.left)
        res += self.serialize(root.right)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(qu):
            val = qu.popleft()
            if val == "#": return
            head = TreeNode(val)
            head.left = helper(qu)
            head.right = helper(qu)
            return head

        data = data.split("_")[:-1]
        q = deque()
        for d in data:
            q.append(d)

        return helper(q)