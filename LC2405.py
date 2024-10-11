class Solution:
    def partitionString(self, s: str) -> int:
        previously_seen_chars = {}
        i = 0
        result = 1
        while i < len(s):
            if previously_seen_chars.get(s[i]) is None:
                previously_seen_chars[s[i]] = 1
                i += 1
            else:
                result += 1
                previously_seen_chars = {}
        return result

