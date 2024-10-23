# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            result = self.findDepth(root)
            return result
        else:
            return 0

    def findDepth(self, root: Optional[TreeNode]) -> int:
        right = 0
        left = 0
        if root.right:
            right = self.findDepth(root.right)
        if root.left:
            left = self.findDepth(root.left)
        if not root.left and not root.right:
            return 1

        return max(right, left) + 1
