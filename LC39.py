from copy import copy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.target = target
        self.generateCombination(candidates, 0,  [])
        return self.result

    def generateCombination(self, candidates, current_sum, current_list):
        for i, candidate in enumerate(candidates):
            current_sum_copy = current_sum
            if current_sum_copy + candidate == self.target:
                current_list_copy = copy(current_list)
                current_list_copy.append(candidate)
                self.result.append(current_list_copy)
            elif current_sum_copy + candidate < self.target:
                current_list_copy = copy(current_list)
                current_list_copy.append(candidate)
                self.generateCombination(candidates[i:], current_sum_copy + candidate, current_list_copy)