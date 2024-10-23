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
        result = ListNode()

        # values_map includes values at HEAD attached to lists[i]
        # we need to initially build the values_map but then can be updated one element at a time

        # linker_map includes the remaining (non- values_map) values in each list
        # once an element of linker_map is depleted it can be popped

        for i, linked_list in enumerate(lists):
            if linked_list:
                values_map[i] = linked_list.val
                linker_map[i] = linked_list.next

        if len(values_map) > 0:
            result.next = curr = ListNode()

        while len(values_map) > 0:
            # take the minimum value in the values_map
            min_idx = min(values_map, key = values_map.get)
            min_val = values_map[min_idx]
            # take the replacement value from
            if linker_map[min_idx] is not None:
                values_map[min_idx] = linker_map[min_idx].val
                linker_map[min_idx] = linker_map[min_idx].next
            else:
                values_map.pop(min_idx)

            curr.val = min_val
            if len(values_map) != 0:
                curr.next = ListNode()
                curr = curr.next

        return result.next