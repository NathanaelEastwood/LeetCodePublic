# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []
        node_list = [[root]]
        i = 0
        while len(node_list) > 0:
            temp = []
            for j in range(len(node_list[i])):
                if node_list[i][j].left:
                    temp.append(node_list[i][j].left)
                if node_list[i][j].right:
                    temp.append(node_list[i][j].right)
            if len(temp) == 0:
                break
            node_list.append(temp)
            i += 1

        for level in node_list:
            result.append(level[-1].val)

        return result