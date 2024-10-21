# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from List_Node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        end_pointer = head
        result = ListNode()

        for i in range(n - 1):
            end_pointer = end_pointer.next

        temporary = dummy

        while end_pointer and end_pointer.next:
            temporary = temporary.next
            end_pointer = end_pointer.next

        temporary.next = None if temporary.next is None else temporary.next.next
        result.next = dummy.next

        return result.next

