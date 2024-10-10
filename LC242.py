class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for i in range(len(s)):
            if s[i] in char_map:
                char_map[s[i]] = char_map[s[i]] + 1
            else:
                char_map[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in char_map:
                return False
            else:
                if char_map[t[j]] < 1:
                    return False
                else:
                    char_map[t[j]] = char_map[t[j]] - 1
                    if char_map[t[j]] == 0:
                        del char_map[t[j]]

        if not bool(char_map):
            return True
        else:
            return False
