from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        for_map = arr.copy()
        for_map.sort()

        map = {}
        start_rank = 1

        for i in range(len(for_map)):
            if map.get(for_map[i]) is None:
                map[for_map[i]] = start_rank
                start_rank += 1

        for j in range(len(arr)):
            arr[j] = map[arr[j]]

        return arr


