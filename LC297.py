# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Optional

from TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        dummy_head = TreeNode()
        curr = TreeNode()
        dummy_head.left = curr
        for i in root:
            curr.val(i)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))