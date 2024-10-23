# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        if not root:
            return True

        if root.left:
            right_depth = self.findDepth(root.left)
            right_balanced = self.isBalanced(root.left)
        else:
            right_depth = 0
            right_balanced = True
        if root.right:
            left_depth = self.findDepth(root.right)
            left_balanced = self.isBalanced(root.right)
        else:
            left_depth = 0
            left_balanced = True

        current_balanced = abs(right_depth - left_depth) < 2

        return current_balanced and left_balanced and right_balanced


    def findDepth(self, root: TreeNode):
        right = 0
        left = 0

        if root.right:
            right = self.findDepth(root.right)
        if root.left:
            left = self.findDepth(root.left)
        if not root.right and not root.left:
            return 1

        return 1 + max(right, left)
