# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional

from List_Node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_map = {}
        while head:
            if node_map.get(head) is not None:
                return True
            else:
                node_map[head] = 1
            head = head.next

        return False
