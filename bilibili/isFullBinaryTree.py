class ResType:
    def __init__(self, height, nodes):
        self.height = height
        self.nodes = nodes


def isFull(root):
    def helper(node):
        if not node: return ResType(0, 0)
        left = helper(node.left)
        right = helper(node.right)
        height = max(left.height, right.height) + 1
        nodes = left.nodes + right.nodes + 1
        return ResType(height, nodes)
    tree = helper(root)
    return tree.nodes == 1 << tree.height -1