from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        def backtrack(current_candidates: List[int], current_nums: List[int], current_sum: int):
            for i, candidate in enumerate(current_candidates):
                current_candidates_copy = current_candidates[::]
                current_nums_copy = current_nums[::]
                current_sum_copy = current_sum
                if current_sum_copy + candidate == target:
                    current_nums_copy.append(candidate)
                    result.append(current_nums_copy)
                elif current_sum_copy + candidate < target:
                    current_nums_copy.append(candidate)
                    current_candidates_copy.pop(i)
                    backtrack(current_candidates_copy, current_nums_copy, current_sum_copy + candidate)

        backtrack(candidates, [], 0)
        return result