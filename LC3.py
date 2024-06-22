class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        output = 0
        for i in range(len(s)):
            s[i] = ord(s[i])

        charSet = set()