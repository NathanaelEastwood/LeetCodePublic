"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional
from Node import Node


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = { None: None }
        pointer1 = head

        while pointer1:
            node_copy = Node(pointer1.val)
            node_map[pointer1] = node_copy
            pointer1 = pointer1.next

        pointer2 = head
        while pointer2:
            node_copy = node_map[pointer2]
            node_copy.next = node_map[pointer2.next]
            node_copy.random = node_map[pointer2.random]
            pointer2 = pointer2.next

        return node_map[head]