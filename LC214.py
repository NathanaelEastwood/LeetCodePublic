from itertools import groupby
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s = list(s)
        result = []

        for k in range(len(s)):
            if s[:k] == list(reversed(s[k+1:(k * 2) + 1])):
                result = list(reversed(s[k+1:]))
                result.extend(s[k:])
            elif s[:k] == list(reversed(s[k:k * 2])):
                result = list(reversed(s[k:]))
                result.extend(s[k:])

        return ''.join(result)
