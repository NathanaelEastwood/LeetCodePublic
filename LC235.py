# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we're looking for a node which is in between p and q, if it is return it.
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root

        left_value = None
        right_value = None
        if root.left:
            left_value = self.dfs(root.left, p, q)
        if root.right:
            right_value = self.dfs(root.right, p, q)
        if not root.right and not root.left:
            return None

        return left_value if left_value else right_value

