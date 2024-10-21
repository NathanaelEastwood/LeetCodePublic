# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from List_Node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, curr = list1, list1
                curr = list1
                list1 = list1.next
            else:
                curr.next, curr = list2, list2
                curr = list2
                list2 = list2.next

        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy.next