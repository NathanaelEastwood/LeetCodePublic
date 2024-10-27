# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.max_sum = -sys.maxsize
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.calculatePathFromNode(root)
        return self.max_sum
    def calculatePathFromNode(self, root: TreeNode):
        # this is our base case - if there are no arms to the tree we return the root's value
        path_left = 0
        path_right = 0
        if root.left:
            path_left = self.calculatePathFromNode(root.left)
        if root.right:
            path_right = self.calculatePathFromNode(root.right)
        elif not root.left:
            self.max_sum = max(self.max_sum, root.val)
            return root.val

        larger_path = max(path_left, path_right)
        self.max_sum = max(path_left + path_right + root.val, self.max_sum)
        self.max_sum = max(max(root.val, root.val + larger_path), self.max_sum)
        return max(root.val, root.val + larger_path)

        # we need to find three things, left path value, right path value and combined value.
        # we only need to return one thing from here, which is the max path value (either left or right), we use the combined value to update self.max_sum