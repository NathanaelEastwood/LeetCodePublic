from typing import Optional
# Definition for singly-linked list.


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Link[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        lr1 = []
        lr2 = []
        # reverse both lists


