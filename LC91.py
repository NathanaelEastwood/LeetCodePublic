from collections import deque


class Solution:
    def numDecodings(self, s: str) -> int:
        # can we keep a cumulative sum?
        