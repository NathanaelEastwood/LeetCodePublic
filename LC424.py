from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        char_map = defaultdict(int)
        l = 0

        for r in range(len(s)):
            char_map[s[r]] += 1

            while (r - l + 1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result