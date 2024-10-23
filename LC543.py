# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(curr: TreeNode):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            nonlocal result
            result = max(result, left + right)
            return max(left, right) + 1

        dfs(root)

        return result