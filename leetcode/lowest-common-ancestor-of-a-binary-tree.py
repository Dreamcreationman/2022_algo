# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def go(self, root, dic):
        if not root:
            return
        dic[root.left] = root
        dic[root.right] = root
        self.go(root.left, dic)
        self.go(root.right, dic)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
        if not root: return
        ancestor = {}
        ancestor[root] = root
        self.go(root, ancestor)

        pf = set()
        cur = p
        while cur != root:
            pf.add(cur)
            cur = ancestor[cur]
        pf.add(root)
        cur = q
        while cur != root:
            if cur in pf: return cur
            cur = ancestor[cur]
        return root

    def lowestCommonAncestor_cur(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
        """
        解释一下这个代码的思路，通过递归来找p，q的位置，（https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/）
        而p，q的位置有三种情况，
            都在左子树 --->
            都在右子树 --->
            一左一右  ---> 那么当前节点就是公共祖先

        然而找到的情况有四种：
            左边找到了东西，右边没找到： 那就说明两节点都在左子树，有可能是在左子树的分开，那么需要递归向下找；要么是其中一个节点就是 公共祖先
            右边找到了东西，左边没找到： 同上
            两边都找到了东西：一左一右，那就对应上面的第三种情况
            两边都没找到东西：说明两节点在该处重合了，那么当前节点就是公共祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return #没找到
        if not left: return right
        if not right: return left
        return root # 一左一右

    def lowestCommonAncestor_bst(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 二叉搜索树版：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
        if not root: return root
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
