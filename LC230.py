# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        stack = deque()
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            i += 1
            if i == k:
                return curr.val
            curr = curr.right




        return result_array[k + 1]
