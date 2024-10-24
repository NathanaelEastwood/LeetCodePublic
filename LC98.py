# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.findValidity(root, float("-inf"), float("inf"))
        return result

    def findValidity(self, root: TreeNode, left_hand_min, right_hand_max):
        if not root:
            return True
        result = left_hand_min < root.val < right_hand_max
        if root.right:
            result = result and self.findValidity(root.right, max(left_hand_min, root.val), right_hand_max)
        if root.left:
            result = result and self.findValidity(root.left, left_hand_min, min(right_hand_max, root.val))
        return result