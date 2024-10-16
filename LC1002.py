from collections import defaultdict
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # build a hashmap for each word
        # loop through the hashmaps comparing each to the first and removing each key which is not equal
        hash_maps = []
        for word in words:
            hash_map = defaultdict(int)
            for char in range(len(word)):
                hash_map[word[char]] += 1
            hash_maps.append(hash_map)

        for i in range(1, len(hash_maps)):
            for key in list(hash_maps[0].keys()):
                if hash_maps[i].get(key) is None:
                    hash_maps[0].pop(key)
                elif hash_maps[0][key] != hash_maps[i][key]:
                    hash_maps[0][key] = min(hash_maps[0][key], hash_maps[i][key])

        result = []
        for key in hash_maps[0]:
            key_values = [key] * hash_maps[0][key]
            result.extend(key_values)

        return result
