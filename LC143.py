# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from List_Node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left_half = head
        right_half = head.next

        while right_half and right_half.next:
            left_half = left_half.next
            right_half = right_half.next.next

        curr = left_half.next
        prev = left_half.next = None

        while curr:
            temporary = curr.next
            curr.next = prev
            prev = curr
            curr = temporary

        left, right = head, prev
        while right:
            temporary1, temporary2 = left.next, right.next
            left.next = right
            right.next = temporary1
            left, right = temporary1, temporary2


        