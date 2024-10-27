from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # the base case is that there will always be a palindrome which is every character in it's own substring
