# Definition for singly-linked list.
from audioop import reverse


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

