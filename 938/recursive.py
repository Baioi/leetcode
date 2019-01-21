# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    num = 0
    def search(self, node, L, R):
        if node.val >= L and node.val <= R:
            self.num += node.val
        if node.left and node.val > L:
            self.search(node.left, L, R)
        if node.right and node.val < R:
            self.search(node.right, L, R)

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.search(root, L, R)
        return self.num
        