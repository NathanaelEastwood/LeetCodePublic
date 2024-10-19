from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = (len(s) + 1, "")
        l = 0
        t_map = defaultdict(int)
        s_map = defaultdict(int)
        for char_t in range(len(t)):
            t_map[t[char_t]] += 1

        r = len(t) - 1
        while r < len(s) or l < len(s):
            # increase the window by moving the right hand pointer forwards until all chars are present,
            # then shrink the window by moving the left hand pointer forwards until the chars are not matched
            window_is_valid = True
            window_length = r-l
            i = 0
            while window_is_valid and i < len(t_map.keys()):
                key = list(t_map.keys())[i]
                if s_map[key] < t_map[key]:
                    window_is_valid = False
                i += 1

            if window_is_valid:
                result = min(result, (window_length, s[l:r]))
            if not window_is_valid and r < len(s):
                s_map[s[r]] += 1
                r += 1
            else:
                s_map[s[l]] -= 1
                l += 1

        return result[1]