# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        
        if root.left:
            left_equality = self.isEqual(root.left, subRoot)
            is_left_subtree = self.isSubtree(root.left, subRoot)
        if root.right:
            right_equality = self.isEqual(root.right, subRoot)
            is_right_subtree = self.isSubtree(root.left, subRoot)

        if root.left == subRoot.left and root.right == subRoot.right:
            return True
        else:
            return left_equality or right_equality or is_left_subtree or is_right_subtree

    def isEqual(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not p.left and not q.left and not p.right and not q.right:
            return True

        left = self.isEqual(p.left, q.left)
        right = self.isEqual(p.right, q.right)

        return left and right