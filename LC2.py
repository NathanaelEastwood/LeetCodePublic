# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from List_Node import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        overflow = 0

        result = ListNode()
        temp = result

        while pointer1 or pointer2:
            pointer1_val = 0 if pointer1 is None else pointer1.val
            pointer2_val = 0 if pointer2 is None else pointer2.val
            val = pointer1_val + pointer2_val + overflow
            if val >= 10:
                temp.next = ListNode(val - 10)
                overflow = 1
            else:
                temp.next = ListNode(val)
                overflow = 0

            temp = temp.next

            pointer1 = None if pointer1 is None else pointer1.next
            pointer2 = None if pointer2 is None else pointer2.next

        if overflow == 1:
            temp.next = ListNode(1)

        return result.next
