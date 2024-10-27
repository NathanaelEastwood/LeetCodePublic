# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we need to split in-order by the first value of the preorder - then we can recursively pass that down to left and right

        for i, node in enumerate(inorder):
            if preorder[0] == node:
                inorder_root_position = i
                break

        inorder_left = inorder[:inorder_root_position]
        inorder_right = inorder[inorder_root_position + 1:]

        root = TreeNode(preorder[0])

        if len(inorder_left) > 0 and len(preorder) > 0:
            # this indicates that there is a tree to the left
            root.left = self.buildTree(preorder[1:], inorder_left)

        if len(inorder_right) > 0 and len(preorder) > 1:
            # this indicates that there is a tree to the right
            root.right = self.buildTree(preorder[len(inorder_left) + 1:], inorder_right)

        return root