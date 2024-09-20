from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False

        target_counts = Counter(target)
        arr_counts = Counter(arr)

        for number in target_counts.keys():
            try:
                if target_counts[number] != arr_counts[number]:
                    return False
            except:
                return False

        return True
