# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
from List_Node import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values_map = {}
        linker_map = {}

        # values_map includes values at HEAD attached to lists[i]
        # we need to initially build the values_map but then can be updated one element at a time

        # linker_map includes the remaining (non- values_map) values in each list
        # once an element of linker_map is depleted it can be popped

        for i, linked_list in enumerate(lists):
            values_map[i] = linked_list.val
            linker_map[i] = linked_list.next

        while len(linker_map) > 0 or len(values_map):
            # take the minimum value in the values_map
            # take the replacement value from 
