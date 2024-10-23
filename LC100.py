# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not p.left and not q.left and not p.right and not q.right:
            return True

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right