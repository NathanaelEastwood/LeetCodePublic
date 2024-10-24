# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = self.countGoodNodes(root, root.val)
        return result + 1

    def countGoodNodes(self, root, current_branch_max):
        good_count = 0

        if root.left:
            good_count += self.countGoodNodes(root.left, max(current_branch_max, root.left.val))
            if root.left.val >= current_branch_max:
                good_count += 1

        if root.right:
            good_count += self.countGoodNodes(root.right, max(current_branch_max, root.right.val))
            if root.right.val >= current_branch_max:
                good_count += 1

        return good_count