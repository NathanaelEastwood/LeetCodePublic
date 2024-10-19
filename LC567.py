from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)
        for i in range(0, len(s1) - 1):
            s1_map[s1[i]] += 1
            s2_map[s1[i]] += 1

        for key in s1_map.keys():
            if s1_map[key] == s2_map[key]:
                matches += s1_map[key]

        left = len(s1)
        right = (len(s1) - 1) * 2

        while right < len(s2):
            if s1_map.get(s2[left]) != 0:




